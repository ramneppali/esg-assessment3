"""ESG message triage: LLM vs rule-based vs Hugging Face zero-shot baselines.

Usage (from the q3 folder):
    python3 triage.py --modes rules                       # no dependencies
    python3 triage.py --modes rules,llm                   # needs an OpenAI-compatible endpoint
    python3 triage.py --modes rules,llm,zeroshot          # zeroshot needs requirements.txt

LLM settings (environment variables, defaults target a local Ollama server):
    LLM_BASE_URL  default http://localhost:11434/v1
    LLM_MODEL     default llama3.1:8b
    LLM_API_KEY   default "ollama" (never hard-code real keys)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"

CATEGORIES = ["WATER", "WASTE_RECYCLING", "ENERGY", "PROCUREMENT_SUPPLIER",
              "ACCESSIBILITY", "GOVERNANCE_CONDUCT", "OTHER"]
URGENCY = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
SENTIMENT = ["POSITIVE", "NEUTRAL", "NEGATIVE"]
TEAMS = ["FACILITIES", "SUSTAINABILITY", "PROCUREMENT", "ACCESSIBILITY_INCLUSION",
         "GOVERNANCE_COMPLIANCE", "NONE"]
SENSITIVITY = ["NONE", "LOW", "HIGH"]

CATEGORY_TO_TEAM = {
    "WATER": "FACILITIES", "ENERGY": "FACILITIES", "WASTE_RECYCLING": "SUSTAINABILITY",
    "PROCUREMENT_SUPPLIER": "PROCUREMENT", "ACCESSIBILITY": "ACCESSIBILITY_INCLUSION",
    "GOVERNANCE_CONDUCT": "GOVERNANCE_COMPLIANCE", "OTHER": "NONE",
}

KEYWORDS = {
    "WATER": ["water", "leak", "flood", "tap", "pipe"],
    "WASTE_RECYCLING": ["recycl", "bin", "waste", "contaminat", "disposal"],
    "ENERGY": ["air conditioning", "lights", "electricity", "energy", "heating"],
    "PROCUREMENT_SUPPLIER": ["supplier", "procure", "vendor", "purchas"],
    "ACCESSIBILITY": ["accessib", "wheelchair", "ramp", "entrance", "lift", "disab"],
    "GOVERNANCE_CONDUCT": ["bribe", "fraud", "harass", "misconduct", "whistle"],
}
HIGH_WORDS = ["all morning", "blocked", "flood", "pooling", "dump", "two days", "unsafe"]
POSITIVE_WORDS = ["thanks", "thank you", "great", "well done"]


def load_messages() -> list[dict]:
    return json.loads((HERE / "messages.json").read_text(encoding="utf-8"))


def rules_classify(text: str) -> dict:
    """Keyword baseline: first category with the most keyword hits wins."""
    low = text.lower()
    scores = {c: sum(k in low for k in kws) for c, kws in KEYWORDS.items()}
    best = max(scores, key=scores.get)
    category = best if scores[best] > 0 else "OTHER"
    positive = any(w in low for w in POSITIVE_WORDS)
    urgency = "LOW" if positive else ("HIGH" if any(w in low for w in HIGH_WORDS) else "MEDIUM")
    return {"issues": [{
        "issue_category": category, "urgency": urgency,
        "sentiment": "POSITIVE" if positive else "NEGATIVE",
        "followup_required": not positive,
        "recommended_team": CATEGORY_TO_TEAM[category],
    }]}


def zeroshot_classify(texts: list[str]) -> list[dict]:
    try:
        from transformers import pipeline
    except ImportError:
        sys.exit("zeroshot mode needs: pip install -r requirements.txt")
    clf = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    out = []
    for t in texts:
        cat = clf(t, candidate_labels=[c.replace("_", " ").lower() for c in CATEGORIES])
        urg = clf(t, candidate_labels=[u.lower() for u in URGENCY])
        category = cat["labels"][0].upper().replace(" ", "_")
        out.append({"issues": [{
            "issue_category": category, "urgency": urg["labels"][0].upper(),
            "recommended_team": CATEGORY_TO_TEAM.get(category, "NONE"),
            "category_score": round(cat["scores"][0], 3),
        }]})
    return out


def extract_json(raw: str) -> dict:
    """Parse a JSON object even if the model wrapped it in fences or prose."""
    raw = re.sub(r"```(?:json)?", "", raw).strip()
    start, end = raw.find("{"), raw.rfind("}")
    if start == -1 or end <= start:
        raise ValueError("no JSON object found")
    return json.loads(raw[start:end + 1])


def validate(result: dict) -> list[str]:
    """Return a list of schema problems (empty list = valid)."""
    problems = []
    issues = result.get("issues")
    if not isinstance(issues, list):
        return ["'issues' missing or not a list"]
    checks = {"issue_category": CATEGORIES, "urgency": URGENCY, "sentiment": SENTIMENT,
              "recommended_team": TEAMS, "data_sensitivity_risk": SENSITIVITY}
    for i, issue in enumerate(issues):
        for field, allowed in checks.items():
            if issue.get(field) not in allowed:
                problems.append(f"issue[{i}].{field}={issue.get(field)!r} not in enum")
        if not isinstance(issue.get("followup_required"), bool):
            problems.append(f"issue[{i}].followup_required is not boolean")
    if not isinstance(result.get("needs_human_review"), bool):
        problems.append("needs_human_review missing or not boolean")
    return problems


def call_llm(prompt: str) -> tuple[str, float]:
    base = os.environ.get("LLM_BASE_URL", "http://localhost:11434/v1").rstrip("/")
    body = json.dumps({
        "model": os.environ.get("LLM_MODEL", "llama3.1:8b"),
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
    }).encode()
    req = urllib.request.Request(
        f"{base}/chat/completions", data=body, method="POST",
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {os.environ.get('LLM_API_KEY', 'ollama')}"})
    started = time.time()
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.load(resp)
    except (urllib.error.URLError, TimeoutError) as exc:
        sys.exit(f"LLM request failed ({exc}). Is the endpoint running / env vars set?")
    return data["choices"][0]["message"]["content"], time.time() - started


def run_llm(messages: list[dict], prompt_file: Path) -> list[dict]:
    template = prompt_file.read_text(encoding="utf-8")
    log = RESULTS / "llm_run_log.jsonl"
    out = []
    for m in messages:
        raw, secs = call_llm(template.replace("{message}", m["text"]))
        try:
            parsed = extract_json(raw)
            problems = validate(parsed)
        except (ValueError, json.JSONDecodeError) as exc:
            parsed, problems = {"issues": []}, [f"unparseable: {exc}"]
        with log.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({"id": m["id"], "model": os.environ.get("LLM_MODEL", "llama3.1:8b"),
                                 "prompt": prompt_file.name, "seconds": round(secs, 2),
                                 "raw": raw, "problems": problems}) + "\n")
        parsed["_schema_problems"] = problems
        out.append(parsed)
    return out


def first(result: dict, field: str) -> str:
    issues = result.get("issues") or [{}]
    return str(issues[0].get(field, "-"))


def write_comparison(messages: list[dict], by_mode: dict[str, list[dict]]) -> None:
    lines = ["| ID | Mode | Category | Urgency | Team |", "|---|---|---|---|---|"]
    for i, m in enumerate(messages):
        for mode, results in by_mode.items():
            r = results[i]
            lines.append(f"| {m['id']} | {mode} | {first(r, 'issue_category')} | "
                         f"{first(r, 'urgency')} | {first(r, 'recommended_team')} |")
    (RESULTS / "comparison.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--modes", default="rules", help="comma list of: rules,llm,zeroshot")
    ap.add_argument("--prompt", default="prompt_v2_revised.txt")
    args = ap.parse_args()

    modes = [m.strip() for m in args.modes.split(",") if m.strip()]
    unknown = set(modes) - {"rules", "llm", "zeroshot"}
    if unknown:
        sys.exit(f"unknown mode(s): {', '.join(sorted(unknown))}")

    RESULTS.mkdir(exist_ok=True)
    messages = load_messages()
    by_mode: dict[str, list[dict]] = {}
    for mode in modes:
        if mode == "rules":
            by_mode[mode] = [rules_classify(m["text"]) for m in messages]
        elif mode == "zeroshot":
            by_mode[mode] = zeroshot_classify([m["text"] for m in messages])
        else:
            by_mode[mode] = run_llm(messages, HERE / args.prompt)
        (RESULTS / f"{mode}_results.json").write_text(
            json.dumps(dict(zip([m["id"] for m in messages], by_mode[mode])), indent=2),
            encoding="utf-8")
    write_comparison(messages, by_mode)


if __name__ == "__main__":
    main()
