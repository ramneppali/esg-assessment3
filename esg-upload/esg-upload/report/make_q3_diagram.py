"""Draw the Q3(d) Azure architecture diagram as a PNG in ../screenshots (needs: pip install pillow).

Usage: python3 make_q3_diagram.py
Draft only. The brief asks for your own diagram, so redraw it in draw.io if required.
"""
from __future__ import annotations

from PIL import Image, ImageDraw

from make_q2_diagrams import (BG_BLUE, BG_GREEN, BG_GREY, BG_RED, GREEN, GREY, NAVY, OUT, RED,
                              arrow_down, box, font)


def line_arrow(d, pts, colour=NAVY):
    d.line(pts, fill=colour, width=5)
    x, y = pts[-1]
    d.polygon([(x - 14, y - 16), (x + 14, y - 16), (x, y)], fill=colour)


def main() -> None:
    img = Image.new("RGB", (1700, 1500), "white")
    d = ImageDraw.Draw(img)
    d.text((60, 30), "Q3(d): Azure architecture for LLM-based ESG message triage", font=font(38, True), fill=NAVY)

    left, right, cx = 60, 900, 480
    box(d, left, 100, right, 215, "Inputs", "Email (Exchange), service portal and Teams messages", BG_GREY, GREY)
    arrow_down(d, cx, 215, 275)
    box(d, left, 275, right, 390, "Azure Logic Apps", "Picks up each new message and starts the workflow", BG_BLUE, NAVY)
    arrow_down(d, cx, 390, 450)
    box(d, left, 450, right, 565, "Azure Service Bus queue", "Buffers spikes, retries failures and holds dead letters", BG_BLUE, NAVY)
    arrow_down(d, cx, 565, 625)
    box(d, left, 625, right, 855, "Azure Functions (orchestrator)", "", BG_BLUE, NAVY,
        body_lines=["Removes personal data before the model call", "Calls Azure OpenAI with the revised prompt",
                    "Validates the JSON and retries if it is invalid", "Sets the review flag from confidence and rules"])

    box(d, 980, 575, 1640, 710, "Azure AI Language", "PII detection and redaction", BG_GREY, GREY)
    box(d, 980, 740, 1640, 900, "Azure OpenAI", "Revised prompt, temperature 0, with Content Safety and Prompt Shields", BG_GREY, GREY)
    d.line((right, 700, 940, 700, 940, 642, 980, 642), fill=GREY, width=4)
    d.line((940, 700, 940, 820, 980, 820), fill=GREY, width=4)

    d.line((cx, 855, cx, 900), fill=NAVY, width=5)
    d.line((265, 900, 705, 900), fill=NAVY, width=5)
    d.text((cx + 16, 862), "needs_human_review?", font=font(24), fill=NAVY)
    d.text((140, 908), "yes", font=font(24, True), fill=RED)
    d.text((725, 908), "no", font=font(24, True), fill=GREEN)
    line_arrow(d, [(265, 900), (265, 945)], RED)
    line_arrow(d, [(705, 900), (705, 945)], GREEN)
    box(d, 60, 945, 470, 1085, "Human review queue", "Power Apps or Teams approval", BG_RED, RED)
    box(d, 510, 945, 900, 1085, "Logic Apps routing", "Teams alert and ServiceNow or Planner ticket", BG_GREEN, GREEN)

    d.line((265, 1085, 265, 1115), fill=NAVY, width=5)
    d.line((705, 1085, 705, 1115), fill=NAVY, width=5)
    d.line((265, 1115, 705, 1115), fill=NAVY, width=5)
    arrow_down(d, cx, 1115, 1170)
    box(d, left, 1170, right, 1285, "Azure Cosmos DB or Azure SQL", "Structured results and audit log", BG_BLUE, NAVY)
    arrow_down(d, cx, 1285, 1345)
    box(d, left, 1345, right, 1460, "Power BI ESG dashboard", "Counts by category, urgency and time to resolve", BG_BLUE, NAVY)

    box(d, 980, 945, 1640, 1285, "Cross-cutting services", "", BG_GREY, GREY,
        body_lines=["Microsoft Entra ID and managed identities", "Key Vault for secrets",
                    "Private endpoints and virtual network", "Azure Monitor and Application Insights",
                    "Microsoft Purview: classification and retention", "Azure Policy"])

    img.save(OUT / "q3_azure_architecture.png")
    print(f"Wrote {OUT / 'q3_azure_architecture.png'}")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    main()
