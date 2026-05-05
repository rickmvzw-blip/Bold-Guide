"""Bold Guide — generate og-image.png + ad creatives + carousel.
Brand palette inherited from index.html (dark + amber gold, Playfair-style serif)."""
import pathlib, math
from PIL import Image, ImageDraw, ImageFont

REPO = pathlib.Path("/Users/ricardomontoya/Workspace/bold_guide")
DESK = pathlib.Path.home() / "Desktop" / "BoldGuide_Marketing"
ADS = DESK / "ads"
CAR = DESK / "carousel"
for p in (DESK, ADS, CAR):
    p.mkdir(parents=True, exist_ok=True)

# --- Brand palette (matches index.html) ---
BG = (10, 10, 8)
SURFACE = (20, 20, 16)
GOLD = (245, 158, 11)
GOLD_DIM = (180, 83, 9)
TEXT = (245, 240, 232)
MUTED = (138, 132, 116)
GREEN = (34, 197, 94)

# --- Fonts ---
PLAYFAIR_PROXY = "/System/Library/Fonts/Supplemental/Baskerville.ttc"  # Playfair-like serif
GEORGIA = "/System/Library/Fonts/Supplemental/Georgia.ttf"
GEORGIA_BOLD = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"
ARIAL_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
MONO = "/System/Library/Fonts/Menlo.ttc"

def fs(size, bold=False, italic=False):  # serif (Playfair-like)
    if bold and italic: idx = 3
    elif italic:        idx = 2
    elif bold:          idx = 1
    else:               idx = 0
    return ImageFont.truetype(PLAYFAIR_PROXY, size=size, index=idx)

def fa(size, bold=False):
    return ImageFont.truetype(ARIAL_BOLD if bold else ARIAL, size=size)

def fm(size):
    return ImageFont.truetype(MONO, size=size, index=0)


def wrap(d, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if d.textlength(test, font=font) <= max_w:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines


# ==========================================================
# 1. og-image.png  (1200x630 — for LinkedIn/X/iMessage previews)
# ==========================================================
def make_og():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # gold corner bracket
    pad, bl = 40, 80
    d.line([(pad, pad+bl), (pad, pad), (pad+bl, pad)], fill=GOLD, width=4)
    d.line([(W-pad-bl, H-pad), (W-pad, H-pad), (W-pad, H-pad-bl)],
           fill=GOLD, width=4)

    label_f = fa(20, bold=True)
    label = "BOLD GUIDE"
    lw = d.textlength(label, font=label_f)
    d.text(((W-lw)/2, 130), label, font=label_f, fill=GOLD, spacing=8)

    head_f = fs(96, bold=True)
    head = "Data. Tools. Results."
    hw = d.textlength(head, font=head_f)
    d.text(((W-hw)/2, 200), head, font=head_f, fill=TEXT)

    sub_f = fs(34, italic=True)
    sub = "Premium digital tools. Pay once, own forever."
    sw = d.textlength(sub, font=sub_f)
    d.text(((W-sw)/2, 360), sub, font=sub_f, fill=MUTED)

    url_f = fa(22, bold=True)
    url = "BOLDGUIDE.IO"
    uw = d.textlength(url, font=url_f)
    d.text(((W-uw)/2, 480), url, font=url_f, fill=GOLD, spacing=6)

    p = REPO / "og-image.png"
    img.save(p, optimize=True)
    print(f"  ✓ {p}")
    # Also copy to marketing
    img.save(DESK / "og-image.png", optimize=True)
    return img


# ==========================================================
# 2. AD CREATIVES — 5 high-end variants for Bold Guide
# ==========================================================
def base_corners(d, W, H, pad=70, bl=100, weight=4):
    d.line([(pad, pad+bl), (pad, pad), (pad+bl, pad)],
           fill=GOLD, width=weight)
    d.line([(W-pad-bl, H-pad), (W-pad, H-pad), (W-pad, H-pad-bl)],
           fill=GOLD, width=weight)


def ad_hero():
    W, H = 1600, 900
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    base_corners(d, W, H, pad=60, bl=110)
    label_f = fa(22, bold=True)
    d.text((W/2 - d.textlength("BOLD GUIDE", font=label_f)/2, 200),
           "BOLD GUIDE", font=label_f, fill=GOLD, spacing=8)
    head = fs(160, bold=True)
    h = "Data. Tools. Results."
    hw = d.textlength(h, font=head)
    d.text(((W-hw)/2, 280), h, font=head, fill=TEXT)
    sub = fs(40, italic=True)
    s = "Premium digital tools for people who move fast."
    sw = d.textlength(s, font=sub)
    d.text(((W-sw)/2, 520), s, font=sub, fill=MUTED)
    url_f = fa(24, bold=True)
    u = "boldguide.io"
    uw = d.textlength(u, font=url_f)
    d.text(((W-uw)/2, 700), u, font=url_f, fill=GOLD, spacing=4)
    img.save(ADS / "01_hero.png")


def ad_manifesto():
    W, H = 1080, 1350
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    base_corners(d, W, H)
    head = fs(110, bold=True)
    lines = ["Buy once.", "Own forever.", "No SaaS tax."]
    y = 380
    for ln in lines:
        lw = d.textlength(ln, font=head)
        d.text(((W-lw)/2, y), ln, font=head, fill=TEXT)
        y += 130
    sub = fs(34, italic=True)
    s = "boldguide.io  —  premium digital tools."
    sw = d.textlength(s, font=sub)
    d.text(((W-sw)/2, y+40), s, font=sub, fill=GOLD)
    img.save(ADS / "02_manifesto.png")


def ad_product_grid():
    W, H = 1200, 1200
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    base_corners(d, W, H, pad=60, bl=90)
    label_f = fa(20, bold=True)
    d.text((W/2 - d.textlength("THE LIBRARY", font=label_f)/2, 130),
           "THE LIBRARY", font=label_f, fill=GOLD, spacing=8)
    head = fs(90, bold=True)
    h = "Two products."
    hw = d.textlength(h, font=head)
    d.text(((W-hw)/2, 190), h, font=head, fill=TEXT)
    h2 = "Both lifetime."
    hw2 = d.textlength(h2, font=head)
    d.text(((W-hw2)/2, 290), h2, font=head, fill=TEXT)

    # Two product cards
    card_w, card_h, gap = 460, 460, 60
    sx = (W - card_w*2 - gap) // 2
    sy = 480
    products = [
        ("LeadForge",     "Lead-enrichment API",     "$97",  GOLD),
        ("ADHD Brain Unlock","150 AI prompts",        "$29",  GREEN),
    ]
    for i,(name, desc, price, accent) in enumerate(products):
        x = sx + i*(card_w+gap)
        d.rounded_rectangle((x, sy, x+card_w, sy+card_h),
                            radius=20, fill=SURFACE,
                            outline=GOLD_DIM, width=1)
        d.rectangle((x, sy, x+card_w, sy+5), fill=accent)
        d.text((x+30, sy+50), name, font=fs(54, bold=True), fill=TEXT)
        d.text((x+30, sy+130), desc, font=fs(28, italic=True), fill=MUTED)
        d.text((x+30, sy+340), price, font=fs(96, bold=True), fill=accent)
        d.text((x+30, sy+440), "lifetime", font=fa(18, bold=True),
               fill=MUTED, spacing=4)
    img.save(ADS / "03_product_grid.png")


def ad_terminal():
    W, H = 1080, 1080
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    base_corners(d, W, H)
    head = fs(72, bold=True)
    h = "Stop renting."
    hw = d.textlength(h, font=head)
    d.text(((W-hw)/2, 200), h, font=head, fill=TEXT)
    h2 = "Start owning."
    hw2 = d.textlength(h2, font=head)
    d.text(((W-hw2)/2, 290), h2, font=head, fill=GOLD)

    # mock terminal
    px, py, pw, ph = 90, 470, W-180, 380
    d.rounded_rectangle((px, py, px+pw, py+ph), radius=18,
                        fill=SURFACE, outline=(40,40,32), width=2)
    for i, c in enumerate([(255,95,86),(255,189,46),(39,201,63)]):
        d.ellipse((px+22+i*26, py+22, px+22+i*26+16, py+22+16), fill=c)
    mono = fm(24)
    lines = [
        ("$ ", "open https://boldguide.io", GREEN),
        ("→ ", "Two lifetime products. Zero subscriptions.", TEXT),
    ]
    y = py + 90
    for prompt, body, color in lines:
        d.text((px+38, y), prompt, font=mono, fill=color)
        d.text((px+38+d.textlength(prompt,font=mono), y),
               body, font=mono, fill=TEXT)
        y += 50
    img.save(ADS / "04_terminal.png")


def ad_linkedin():
    W, H = 1200, 627
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    base_corners(d, W, H, pad=40, bl=70)
    head = fs(72, bold=True)
    h = "Premium tools. Lifetime access."
    hw = d.textlength(h, font=head)
    d.text(((W-hw)/2, 220), h, font=head, fill=TEXT)
    sub = fs(28, italic=True)
    s = "Bold Guide — built for people who move fast."
    sw = d.textlength(s, font=sub)
    d.text(((W-sw)/2, 340), s, font=sub, fill=MUTED)
    url_f = fa(22, bold=True)
    u = "BOLDGUIDE.IO"
    uw = d.textlength(u, font=url_f)
    d.text(((W-uw)/2, 460), u, font=url_f, fill=GOLD, spacing=6)
    img.save(ADS / "05_linkedin.png")


# ==========================================================
# 3. CAROUSEL (8 slides) — 1080x1080
# ==========================================================
W, H = 1080, 1080
PAD = 90
BL = 110

def carousel_base(num):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.line([(PAD, PAD+BL), (PAD, PAD), (PAD+BL, PAD)],
           fill=GOLD, width=5)
    d.line([(W-PAD-BL, H-PAD), (W-PAD, H-PAD),
            (W-PAD, H-PAD-BL)], fill=GOLD, width=5)
    foot = fa(22, bold=True)
    txt = f"BOLDGUIDE.IO  ·  {num}/8"
    tw = d.textlength(txt, font=foot)
    d.text(((W-tw)/2, H-60), txt, font=foot, fill=MUTED, spacing=2)
    return img, d


def cs(num, name, head, sub=None, custom=None):
    img, d = carousel_base(num)
    if custom:
        custom(img, d)
    else:
        max_w = W - 2*PAD - 60
        head_f = fs(78, bold=True)
        sub_f = fs(36, italic=True)
        hl = wrap(d, head, head_f, max_w)
        block_h = len(hl) * 88
        if sub:
            sl = wrap(d, sub, sub_f, max_w)
            block_h += 50 + len(sl) * 50
        y = (H - block_h) // 2 - 30
        for ln in hl:
            d.text((PAD+30, y), ln, font=head_f, fill=TEXT); y += 88
        if sub:
            y += 50
            for ln in sl:
                d.text((PAD+30, y), ln, font=sub_f, fill=MUTED); y += 50
    img.save(CAR / f"slide_{num}_{name}.png")
    print(f"  ✓ slide_{num}_{name}.png")


# clear existing
for p in CAR.glob("slide_*.png"): p.unlink()

# Slide 1 — cover
cs(1, "cover",
   "What if every tool you bought was yours forever?",
   "Welcome to Bold Guide.")

# Slide 2 — pain
cs(2, "pain",
   "The average creator pays for 47 SaaS subscriptions.",
   "$3,000+ per year. Most go unused. All keep auto-renewing.")

# Slide 3 — thesis
cs(3, "thesis",
   "We built the alternative.",
   "Premium digital tools. One-time payment. Lifetime access.")

# Slide 4 — Products header
cs(4, "products",
   "Two products. Both lifetime.")

# Slide 5 — LeadForge
def slide5(img, d):
    label = "PRODUCT 01"
    lf = fa(20, bold=True)
    lw = d.textlength(label, font=lf)
    d.text((PAD+30, 200), label, font=lf, fill=GOLD, spacing=4)
    head = "LeadForge"
    d.text((PAD+30, 260), head, font=fs(110, bold=True), fill=TEXT)
    sub = "B2B lead-enrichment + workflow API"
    d.text((PAD+30, 420), sub, font=fs(36, italic=True), fill=MUTED)
    price = "$97"
    pw = d.textlength(price, font=fs(160, bold=True))
    d.text((PAD+30, 580), price, font=fs(160, bold=True), fill=GOLD)
    d.text((PAD+30+pw+30, 670), "lifetime",
           font=fa(24, bold=True), fill=MUTED, spacing=4)
cs(5, "leadforge", "", custom=slide5)

# Slide 6 — ADHD Brain Unlock
def slide6(img, d):
    label = "PRODUCT 02"
    lf = fa(20, bold=True)
    d.text((PAD+30, 200), label, font=lf, fill=GREEN, spacing=4)
    head = "ADHD Brain"
    d.text((PAD+30, 260), head, font=fs(96, bold=True), fill=TEXT)
    head2 = "Unlock"
    d.text((PAD+30, 360), head2, font=fs(96, bold=True), fill=TEXT)
    sub = "150 AI prompts for focus, momentum, and execution."
    sublines = wrap(d, sub, fs(32, italic=True), W-2*PAD-60)
    y = 480
    for ln in sublines:
        d.text((PAD+30, y), ln, font=fs(32, italic=True), fill=MUTED)
        y += 44
    price = "$29"
    pw = d.textlength(price, font=fs(160, bold=True))
    d.text((PAD+30, 620), price, font=fs(160, bold=True), fill=GREEN)
    d.text((PAD+30+pw+30, 710), "lifetime",
           font=fa(24, bold=True), fill=MUTED, spacing=4)
cs(6, "adhd_brain", "", custom=slide6)

# Slide 7 — Why
cs(7, "why",
   "Why lifetime?",
   "Because the marginal cost of digital is zero. Charging $99/mo for it is theft.")

# Slide 8 — CTA
def slide8(img, d):
    head_f = fs(96, bold=True)
    heads = ["Bold Guide.", "Open library."]
    y = 320
    for ln in heads:
        lw = d.textlength(ln, font=head_f)
        d.text(((W-lw)/2, y), ln, font=head_f, fill=TEXT)
        y += 110
    sub = "boldguide.io"
    sw = d.textlength(sub, font=fs(40, italic=True))
    d.text(((W-sw)/2, y+40), sub, font=fs(40, italic=True), fill=GOLD)
    btn_f = fa(26, bold=True)
    btn = "BROWSE THE LIBRARY  →"
    btn_w = d.textlength(btn, font=btn_f)
    bw, bh = int(btn_w + 80), 70
    bx = (W-bw)//2; by = 780
    d.rounded_rectangle((bx, by, bx+bw, by+bh), radius=35, fill=GOLD)
    d.text((bx+(bw-btn_w)/2, by+22), btn, font=btn_f, fill=BG, spacing=3)
cs(8, "cta", "", custom=slide8)


# ==========================================================
# Build PDF
# ==========================================================
slides = sorted(CAR.glob("slide_*.png"))
imgs = [Image.open(s).convert("RGB") for s in slides]
pdf = DESK / "BoldGuide_Carousel.pdf"
imgs[0].save(pdf, save_all=True, append_images=imgs[1:],
             format="PDF", resolution=150.0)
print(f"\n  ✓ {pdf}")


# ==========================================================
# Run all
# ==========================================================
print("OG image:")
make_og()
print("\nAds:")
ad_hero();        print("  ✓ 01_hero.png")
ad_manifesto();   print("  ✓ 02_manifesto.png")
ad_product_grid();print("  ✓ 03_product_grid.png")
ad_terminal();    print("  ✓ 04_terminal.png")
ad_linkedin();    print("  ✓ 05_linkedin.png")
print(f"\nDONE → {DESK}")
