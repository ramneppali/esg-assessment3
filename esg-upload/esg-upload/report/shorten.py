"""Make a condensed copy of Assessment3_Report.md text for the short Word file.

The full report stays unchanged. This keeps every question answered and cuts
supporting detail: repeated screenshots, the ASCII flow diagram, two of the
four example transcripts, the video script and the optional extension.
"""
from __future__ import annotations

import re

# Original figure numbers removed from the short version.
DROP_FIGURES = {1, 3, 4, 5, 6, 7, 8, 9, 12, 13, 15, 16, 17, 18, 22, 23, 25, 26, 27, 28}

# Whole lines (table rows, bullets, short paragraphs) removed when they start with these.
DROP_LINE_PREFIXES = (
    "Both custom entities are Map entities",
    "| Form re-prompts |",
    "| No-input |",
    "| Endpoint |",
    "- **Agreement:**",
    "- **Cost and speed:**",
    "- **Category:** The zero-shot",
    "- **Team:** The zero-shot",
    "- **Limit:** Five messages",
    "- **Accessibility benefit:**",
    "- **Practical limits:**",
)

NOTE = (
    "*This is the condensed version of the report. Every question is answered. "
    "Extra screenshots, two example transcripts and some outputs are left out and "
    "are in the full report and the repository.*"
)


def _sub_once(pattern: str, repl: str, text: str, flags: int = 0) -> str:
    new, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise ValueError(f"shorten.py: section not found, update the pattern: {pattern[:60]}")
    return new


def shorten(text: str) -> str:
    # Condensed-version notice after the artefact table.
    text = _sub_once(r"(\| GitHub repository[^\n]*\n)", r"\1\n" + NOTE.replace("\\", "\\\\") + "\n", text)

    # Q1(c): ASCII conversation map replaced by the flow visualiser screenshot.
    text = _sub_once(
        r"#### Conversation map\n\n```.*?```\n\nThe diagram above is the design\. The screenshots below show",
        "#### Conversation map\n\nThe screenshot below shows",
        text,
        re.S,
    )

    # Q1(c): transcripts 3 and 4 summarised in one sentence.
    text = _sub_once(
        r"\*\*Transcript 3: request for a person\*\*.*?(?=#### Test results and reflection)",
        "Two further tests behaved as designed: \"talk to a person\" routed to the Human Handoff page, "
        "and \"what can you do\" returned the scope message and stayed on the Start Page.\n\n",
        text,
        re.S,
    )

    # Q1(c): optional extension section.
    text = _sub_once(r"#### Optional extension: connection to cloud workflows.*?(?=### Q1\(d\))", "", text, re.S)

    # Q1(e): suggested video script.
    text = _sub_once(r"Suggested 100-second script.*?(?=---\n\n## Q2)", "", text, re.S)

    # Q3(a): keep the M1 output, point to the results folder for M2 and M3.
    text = _sub_once(
        r"M2, supplier dumping waste in a river:.*?(?=\*\*Original prompt output for contrast)",
        "The M2 and M3 outputs are in `q3/results/`.\n\n",
        text,
        re.S,
    )

    # Q4(a): shorter note on feature availability.
    text = _sub_once(
        r"\*Feature availability and limits change often\..*?\* I used the free plan",
        "Feature availability and limits change often, so this report describes the features as tested "
        "on 7 October 2026. I used the free plan",
        text,
        re.S,
    )

    # Whole-line cuts. Each prefix must match, so changes to the full report are noticed.
    lines = text.splitlines()
    for prefix in DROP_LINE_PREFIXES:
        n_before = len(lines)
        lines = [ln for ln in lines if not ln.startswith(prefix)]
        if len(lines) == n_before:
            raise ValueError(f"shorten.py: line not found, update DROP_LINE_PREFIXES: {prefix}")
    text = "\n".join(lines) + "\n"

    # Figures: drop some, renumber the rest, and fix in-text references.
    kept = []
    out = []
    for line in text.splitlines():
        m = re.match(r"!\[Figure (\d+)\. ", line)
        if m:
            n = int(m.group(1))
            if n in DROP_FIGURES:
                continue
            kept.append(n)
        out.append(line)
    new_no = {old: i for i, old in enumerate(kept, 1)}
    text = "\n".join(out) + "\n"
    text = re.sub(r"\n{3,}", "\n\n", text)

    def renumber(m: re.Match) -> str:
        n = int(m.group(1))
        if n in new_no:
            return f"Figure {new_no[n]}"
        return "screenshot in `q4/screenshots/`"

    return re.sub(r"Figure (\d+)", renumber, text)
