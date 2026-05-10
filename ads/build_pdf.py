"""Build a print-ready PDF of the Bold Guide ad-link reference from the CSV.

Run: /usr/bin/python3 ads/build_pdf.py
Output: ads/bold-guide-ad-links.pdf
"""
import csv
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
)

NAVY = colors.HexColor("#1B2A4E")
AMBER = colors.HexColor("#E8A33D")
GRAY = colors.HexColor("#8B8B8B")
BG = colors.HexColor("#FBFAF7")
INK = colors.HexColor("#0F1A33")

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "bold-guide-ad-links.csv")
PDF_PATH = os.path.join(HERE, "bold-guide-ad-links.pdf")


def read_groups():
    groups = []
    current = None
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # header
        for row in reader:
            if not any(c.strip() for c in row):
                current = None
                continue
            product, channel, src, med, camp, url = row
            if current is None or current["product"] != product:
                current = {"product": product, "rows": []}
                groups.append(current)
            current["rows"].append({
                "channel": channel, "src": src, "med": med,
                "camp": camp, "url": url,
            })
    return groups


def build():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
        title="Bold Guide LLC — Ad Link Reference",
        author="Bold Guide LLC",
    )
    styles = getSampleStyleSheet()
    h1 = ParagraphStyle(
        "h1", parent=styles["Heading1"], fontName="Helvetica-Bold",
        fontSize=20, textColor=NAVY, spaceAfter=2, leading=24,
    )
    sub = ParagraphStyle(
        "sub", parent=styles["Normal"], fontName="Helvetica",
        fontSize=9, textColor=GRAY, spaceAfter=14,
    )
    h2 = ParagraphStyle(
        "h2", parent=styles["Heading2"], fontName="Helvetica-Bold",
        fontSize=13, textColor=NAVY, spaceBefore=10, spaceAfter=4,
    )
    body = ParagraphStyle(
        "body", parent=styles["Normal"], fontName="Helvetica",
        fontSize=9, textColor=INK, leading=12,
    )
    foot = ParagraphStyle(
        "foot", parent=styles["Normal"], fontName="Helvetica",
        fontSize=8, textColor=GRAY, leading=11, alignment=1,
    )

    story = []
    story.append(Paragraph("Bold Guide LLC <font color='#E8A33D'>·</font> Ad Link Reference", h1))
    story.append(Paragraph(
        "Paste these exact URLs into ad creatives. UTM tags auto-track which channel drove each visit.",
        sub,
    ))

    groups = read_groups()
    for g in groups:
        story.append(Paragraph(g["product"], h2))
        data = [["Channel", "Campaign", "URL"]]
        for r in g["rows"]:
            channel = r["channel"] or "—"
            camp = r["camp"] or "—"
            url = r["url"]
            # Wrap long URLs by inserting zero-width break points
            url_para = Paragraph(
                f'<font face="Courier" size="7">{url}</font>',
                ParagraphStyle("u", fontName="Courier", fontSize=7, leading=9, textColor=INK),
            )
            data.append([
                Paragraph(channel, body),
                Paragraph(f'<font size="7">{camp}</font>', body),
                url_para,
            ])
        tbl = Table(
            data,
            colWidths=[1.5 * inch, 1.8 * inch, 4.2 * inch],
            repeatRows=1,
        )
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 9),
            ("ALIGN", (0, 0), (-1, 0), "LEFT"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
            ("TOPPADDING", (0, 0), (-1, 0), 6),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, BG]),
            ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#E5E5E5")),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 1), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 4),
        ]))
        story.append(tbl)
        story.append(Spacer(1, 0.08 * inch))

    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph(
        "Bold Guide LLC &nbsp;·&nbsp; ricardo@boldguide.io &nbsp;·&nbsp; (951) 544-9913 &nbsp;·&nbsp; "
        "P.O. Box 312, Rialto, CA 92377",
        foot,
    ))

    doc.build(story)
    print(f"wrote {PDF_PATH} ({os.path.getsize(PDF_PATH)} bytes)")


if __name__ == "__main__":
    build()
