"""Draw the two Q2 diagrams as PNGs in ../screenshots (needs: pip install pillow).

Usage: python3 make_q2_diagrams.py
These are drafts built from the Mandiant (2024) post. Redraw them in your own style if the brief asks for original work.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Install Pillow first: pip install pillow")

OUT = Path(__file__).resolve().parent.parent / "screenshots"
FONT_PATHS = ["/System/Library/Fonts/Helvetica.ttc", "/System/Library/Fonts/Supplemental/Arial.ttf"]

NAVY, RED, GREY, GREEN = "#1f3a5f", "#b3261e", "#5f6368", "#1e6b3a"
BG_BLUE, BG_RED, BG_GREY, BG_GREEN = "#e8f0fb", "#fdecea", "#f1f3f4", "#e6f4ea"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    for path in FONT_PATHS:
        try:
            return ImageFont.truetype(path, size, index=1 if bold and path.endswith(".ttc") else 0)
        except OSError:
            continue
    return ImageFont.load_default(size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt, max_w: int) -> list[str]:
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def box(draw, x0, y0, x1, y1, title, body, fill, outline, body_lines=None):
    draw.rounded_rectangle((x0, y0, x1, y1), radius=18, fill=fill, outline=outline, width=4)
    pad, y = 24, y0 + 20
    draw.text((x0 + pad, y), title, font=font(30, True), fill=outline)
    y += 48
    lines = body_lines or wrap(draw, body, font(26), x1 - x0 - 2 * pad)
    for line in lines:
        draw.text((x0 + pad, y), line, font=font(26), fill="#202124")
        y += 36


def arrow_down(draw, x, y0, y1, label=""):
    draw.line((x, y0, x, y1 - 14), fill=NAVY, width=5)
    draw.polygon([(x - 14, y1 - 16), (x + 14, y1 - 16), (x, y1)], fill=NAVY)
    if label:
        draw.text((x + 24, (y0 + y1) // 2 - 16), label, font=font(24), fill=NAVY)


def attack_flow() -> None:
    img = Image.new("RGB", (1600, 1280), "white")
    d = ImageDraw.Draw(img)
    d.text((60, 30), "Snowflake customer data theft campaign (UNC5537): attack path", font=font(38, True), fill=NAVY)

    left, right = 60, 980
    box(d, left, 110, right, 300, "1. Credential theft",
        "Infostealer malware on contractor and employee devices captures Snowflake usernames and passwords. "
        "Some credentials were stolen as far back as 2020.", BG_BLUE, NAVY)
    arrow_down(d, 520, 300, 380, "stolen credentials")
    box(d, left, 380, right, 570, "2. Login to the customer's Snowflake account",
        "The attacker logs in over the internet with only a valid username and password, using "
        "Snowsight, SnowSQL or DBeaver, often through VPN addresses.", BG_BLUE, NAVY)
    arrow_down(d, 520, 570, 650, "valid login accepted")
    box(d, left, 650, right, 880, "3. Reconnaissance and export (customer SaaS account)",
        "", BG_BLUE, NAVY,
        body_lines=["SHOW TABLES: list databases and tables", "SELECT: read tables of interest",
                    "CREATE TEMPORARY STAGE, COPY INTO: stage and compress data",
                    "GET: download the data to the attacker's machine"])
    arrow_down(d, 520, 880, 960, "bulk export")
    box(d, left, 960, right, 1150, "4. Monetisation",
        "The stolen data is advertised for sale on cybercrime forums and victims are extorted.", BG_RED, RED)

    box(d, 1040, 380, 1540, 600, "Missing controls", "", BG_RED, RED,
        body_lines=["No multi-factor authentication", "Credentials never rotated",
                    "No network allow-list"])
    d.line((right, 475, 1040, 475), fill=RED, width=4)

    box(d, 1040, 650, 1540, 880, "Snowflake platform", "", BG_GREY, GREY,
        body_lines=["Runs on a public cloud (IaaS).", "Provider-managed.", "Mandiant found no breach",
                    "of Snowflake's own environment."])
    d.line((right, 765, 1040, 765), fill=GREY, width=4)

    d.text((60, 1200), "Source: Mandiant (2024), UNC5537 targets Snowflake customer instances for data theft and extortion.",
           font=font(22), fill=GREY)
    img.save(OUT / "q2_attack_flow.png")


def shared_responsibility() -> None:
    img = Image.new("RGB", (1600, 860), "white")
    d = ImageDraw.Draw(img)
    d.text((60, 30), "Shared responsibility for Snowflake (SaaS on public cloud IaaS)", font=font(38, True), fill=NAVY)

    bands = [
        ("Customer", RED, BG_RED, [
            "Users, passwords and MFA enrolment",
            "Network policy and access restrictions",
            "Data classification, access and exports",
            "Endpoint security, including contractor devices",
            "Monitoring of login and query activity"]),
        ("Snowflake (SaaS provider)", NAVY, BG_BLUE, [
            "Platform software, patching and availability",
            "Provides MFA, network policies and logging",
            "(the customer must switch them on)"]),
        ("Cloud provider (AWS, Azure or GCP)", GREEN, BG_GREEN, [
            "Physical data centres, hardware and hypervisor"]),
    ]
    y = 110
    for title, colour, fill, items in bands:
        h = 60 + 40 * len(items)
        d.rounded_rectangle((60, y, 1540, y + h), radius=18, fill=fill, outline=colour, width=4)
        d.text((90, y + 22), title, font=font(30, True), fill=colour)
        for i, item in enumerate(items):
            d.text((700, y + 22 + 40 * i), item, font=font(26), fill="#202124")
        y += h + 30

    d.text((60, y), "In the UNC5537 incidents the failures sat in the customer layer: identity, network access and monitoring.",
           font=font(26, True), fill=RED)
    d.text((60, y + 50), "Sources: Mell and Grance (2011); AWS (n.d.); Mandiant (2024).", font=font(22), fill=GREY)
    img.save(OUT / "q2_shared_responsibility.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    attack_flow()
    shared_responsibility()
    print(f"Wrote diagrams to {OUT}")
