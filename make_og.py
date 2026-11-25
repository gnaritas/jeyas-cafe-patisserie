#!/usr/bin/env python3
"""og.png 1200x630 — JEYAS Café & Pâtisserie — vitrine poster.
Espresso noir, cream serif, antique-gold hairlines, bordeaux rule. Shop identity only.
Every line is measured and center-fitted; the script FAILS if any line would collide."""
from PIL import Image, ImageDraw, ImageFont
import os, sys

W, H = 1200, 630
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

NOIR = (34, 26, 21); NOIR2 = (26, 19, 15); CREAM = (247, 241, 228)
GOLD = (185, 143, 69); GOLD2 = (150, 116, 58); BORDEAUX = (140, 60, 52); MUTE = (154, 138, 112)

def font(paths, size):
    bases = ["/System/Library/Fonts/Supplemental/", "/System/Library/Fonts/"]
    for b in bases:
        for n in paths:
            p = b + n
            if os.path.exists(p):
                try: return ImageFont.truetype(p, size)
                except Exception: pass
    return ImageFont.load_default()

serif = lambda s: font(["Iowan Old Style.ttc", "Palatino.ttc", "Georgia.ttf", "Times New Roman.ttf"], s)
sans = lambda s: font(["Futura.ttc", "HelveticaNeue.ttc", "Arial Bold.ttf", "Arial.ttf"], s)
mono = lambda s: font(["Menlo.ttc", "Consolas", "Monaco.dfont", "Courier New.ttf"], s)

img = Image.new("RGB", (W, H), NOIR)
d = ImageDraw.Draw(img)

# lower band = the counter (deeper noir)
d.rectangle([0, 492, W, H], fill=NOIR2)
# gold rails top + bottom
d.rectangle([0, 0, W, 6], fill=GOLD)
d.rectangle([0, H-6, W, H], fill=GOLD)
# inner hairline frame
d.rectangle([26, 26, W-26, H-26], outline=GOLD2, width=1)

widths = []
def center(text, f, y, fill, tracking=0):
    if tracking:
        cw = [d.textbbox((0,0), ch, font=f)[2]-d.textbbox((0,0), ch, font=f)[0] for ch in text]
        tw = sum(cw) + tracking*(len(text)-1)
        x = (W-tw)/2
        for ch,w_ in zip(text,cw):
            bb = d.textbbox((0,0), ch, font=f)
            d.text((x - bb[0], y), ch, font=f, fill=fill)
            x += w_ + tracking
        widths.append((y, tw))
        return tw
    bb = d.textbbox((0,0), text, font=f)
    tw = bb[2]-bb[0]
    d.text(((W-tw)/2 - bb[0], y), text, font=f, fill=fill)
    widths.append((y, tw))
    return tw

# kicker
center("OPENING SPRING 2027  ·  THE ICE BLOCKS  ·  SACRAMENTO", mono(22), 46, GOLD, tracking=4)

# brand — cream serif monogram + gold tracking subline
tw = center("JEYAS", serif(150), 96, CREAM, tracking=18)
center("CAF\u00c9  &  P\u00c2TISSERIE", sans(31), 272, GOLD, tracking=13)

# dashed bordeaux rule under brand
for i in range(0, 300, 24):
    x = W/2 - 150 + i
    d.rectangle([x, 336, x+13, 339], fill=BORDEAUX)

# tagline lines — serif, cream + bordeaux-bright
center("Croissants baked in-house before dawn.", serif(43), 362, CREAM)
center("Cr\u00eapes and dessert until midnight.", serif(43), 422, (206, 116, 100))

# counter band strips — measured single rows
center("Croissants  \u00b7  Cr\u00eapes  \u00b7  Specialty Coffee  \u00b7  Smoothies  \u00b7  A\u00e7a\u00ed", sans(25), 508, CREAM)
center("1710 R Street \u00b7 Sacramento \u00b7 planned 6:30 a.m.\u2013midnight, daily", mono(20), 546, GOLD)
center("From the family behind Jayna Gyro \u2014 Jeyda, Yasemin & Ashley", mono(20), 580, MUTE)

img.save(OUT, "PNG", optimize=True)

# collision guard: no line may exceed the safe box (W-110 inside the hairline frame)
bad = [(y, tw) for y, tw in widths if tw > W-110]
if bad:
    for y, tw in bad: print("OVERWIDE", y, tw, file=sys.stderr)
    sys.exit(1)
print("wrote", OUT, os.path.getsize(OUT), "bytes; widest line:", max(tw for _, tw in widths), "px (safe box", W-110, ")")
