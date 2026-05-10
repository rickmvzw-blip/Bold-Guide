"""Build a free 5-prompt sampler PDF teaser of the ADHD Brain Unlock pack.

Run: /usr/bin/python3 ads/build_sampler.py
Output: ads/adhd-5-free-prompts-sampler.pdf
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
)
from reportlab.lib.enums import TA_CENTER

NAVY = colors.HexColor("#1B2A4E")
AMBER = colors.HexColor("#E8A33D")
GRAY = colors.HexColor("#8B8B8B")
BG = colors.HexColor("#FBFAF7")
INK = colors.HexColor("#0F1A33")

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(HERE, "adhd-5-free-prompts-sampler.pdf")

PROMPTS = [
    {
        "n": 1,
        "title": "Soft-start morning routine",
        "body": (
            "I have ADHD and I just woke up. Help me create a simple 3-step "
            "morning routine that takes under 20 minutes and gets me ready to focus."
        ),
    },
    {
        "n": 2,
        "title": "Brain-dump template",
        "body": (
            "Write me a 5-minute morning brain dump template I can use to clear "
            "my head before starting work."
        ),
    },
    {
        "n": 3,
        "title": "Recovery from a late start",
        "body": (
            "I woke up late and feel behind. Help me do a quick reset so I can "
            "salvage the rest of my day without spiraling."
        ),
    },
    {
        "n": 4,
        "title": "Launch sequence ritual",
        "body": (
            "Help me write a 'launch sequence' \u2014 a personal ritual that signals "
            "to my brain it's time to work."
        ),
    },
    {
        "n": 5,
        "title": "Minimum viable morning",
        "body": (
            "Create a 'minimum viable morning' routine \u2014 the bare minimum I need "
            "to do to have a productive day."
        ),
    },
]


def build():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        title="ADHD Brain Unlock — 5 Free Prompts",
        author="Bold Guide LLC",
    )
    styles = getSampleStyleSheet()
    h1 = ParagraphStyle(
        "h1", parent=styles["Heading1"], fontName="Helvetica-Bold",
        fontSize=24, textColor=NAVY, alignment=TA_CENTER,
        spaceAfter=2, leading=28,
    )
    eyebrow = ParagraphStyle(
        "eyebrow", parent=styles["Normal"], fontName="Helvetica-Bold",
        fontSize=10, textColor=AMBER, alignment=TA_CENTER,
        spaceAfter=4, leading=12,
    )
    sub = ParagraphStyle(
        "sub", parent=styles["Normal"], fontName="Helvetica",
        fontSize=10, textColor=GRAY, alignment=TA_CENTER,
        spaceAfter=18, leading=14,
    )
    pn = ParagraphStyle(
        "pn", parent=styles["Normal"], fontName="Helvetica-Bold",
        fontSize=10, textColor=AMBER, leading=14, spaceAfter=2,
    )
    pt = ParagraphStyle(
        "pt", parent=styles["Normal"], fontName="Helvetica-Bold",
        fontSize=13, textColor=NAVY, leading=16, spaceAfter=6,
    )
    pb = ParagraphStyle(
        "pb", parent=styles["Normal"], fontName="Helvetica",
        fontSize=11, textColor=INK, leading=16, spaceAfter=4,
    )
    note = ParagraphStyle(
        "note", parent=styles["Normal"], fontName="Helvetica-Oblique",
        fontSize=9, textColor=GRAY, leading=12, spaceAfter=14,
    )
    cta_title = ParagraphStyle(
        "ctaTitle", parent=styles["Heading2"], fontName="Helvetica-Bold",
        fontSize=18, textColor=colors.white, alignment=TA_CENTER,
        spaceAfter=4, leading=22,
    )
    cta_sub = ParagraphStyle(
        "ctaSub", parent=styles["Normal"], fontName="Helvetica",
        fontSize=11, textColor=colors.HexColor("#FBFAF7"), alignment=TA_CENTER,
        spaceAfter=8, leading=15,
    )
    cta_url = ParagraphStyle(
        "ctaUrl", parent=styles["Normal"], fontName="Helvetica-Bold",
        fontSize=13, textColor=AMBER, alignment=TA_CENTER,
        spaceAfter=2, leading=16,
    )
    foot = ParagraphStyle(
        "foot", parent=styles["Normal"], fontName="Helvetica",
        fontSize=8, textColor=GRAY, leading=11, alignment=TA_CENTER,
    )

    story = []
    story.append(Paragraph("BOLD GUIDE LLC", eyebrow))
    story.append(Paragraph("ADHD Brain Unlock", h1))
    story.append(Paragraph(
        "5 free prompts from the 150-prompt pack &nbsp;·&nbsp; "
        "Copy. Paste. Get unstuck.",
        sub,
    ))

    story.append(Paragraph(
        "Works with ChatGPT, Claude, Gemini, or any AI assistant. Open one, paste "
        "the prompt, and let it walk you through the next step. Swap anything in "
        "[brackets] for your own details.",
        note,
    ))

    for p in PROMPTS:
        story.append(Paragraph(f"PROMPT {p['n']:02d}", pn))
        story.append(Paragraph(p["title"], pt))
        story.append(Paragraph(f'\u201c{p["body"]}\u201d', pb))
        story.append(Spacer(1, 0.12 * inch))

    story.append(Spacer(1, 0.15 * inch))

    # CTA box
    cta_cell = [
        [Paragraph("Want the other 145?", cta_title)],
        [Paragraph(
            "8 categories. 150 plug-and-play prompts. Lifetime access for $27.",
            cta_sub,
        )],
        [Paragraph(
            "boldguide.io/adhd150prompts/",
            cta_url,
        )],
        [Paragraph(
            "24-hour money-back guarantee &nbsp;·&nbsp; instant download",
            ParagraphStyle("g", parent=styles["Normal"], fontName="Helvetica",
                           fontSize=9, textColor=colors.HexColor("#FBFAF7"),
                           alignment=TA_CENTER, leading=12),
        )],
    ]
    cta_tbl = Table(cta_cell, colWidths=[7.0 * inch])
    cta_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 18),
        ("RIGHTPADDING", (0, 0), (-1, -1), 18),
        ("TOPPADDING", (0, 0), (0, 0), 18),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 18),
        ("BOX", (0, 0), (-1, -1), 1, AMBER),
    ]))
    story.append(cta_tbl)

    story.append(Spacer(1, 0.25 * inch))
    story.append(Paragraph(
        "Bold Guide LLC &nbsp;·&nbsp; ricardo@boldguide.io &nbsp;·&nbsp; "
        "Not medical advice. For coaching and productivity support only.",
        foot,
    ))

    doc.build(story)
    print(f"wrote {PDF_PATH} ({os.path.getsize(PDF_PATH)} bytes)")


if __name__ == "__main__":
    build()
