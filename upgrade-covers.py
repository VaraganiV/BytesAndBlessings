#!/usr/bin/env python3
"""Regenerate cover SVGs with professional, distinct category colors"""
import os, re
from pathlib import Path

site = Path.home() / "Factory" / "BytesAndBlessings" / "site"
posts = site / "content" / "posts"
covers_dir = site / "static" / "images" / "covers"
covers_dir.mkdir(parents=True, exist_ok=True)

# Professional color palettes per category
PALETTES = {
    "tech": ("#0f2b46", "#1a4d7a", "#2670a8"),
    "sanatana-dharma": ("#1a1033", "#2d1b5e", "#4a2d8a"),
    "temple-trails": ("#2d0a3e", "#5c1a8a", "#8b3dc4"),
    "shorts": ("#0a3333", "#136060", "#1a9090"),
    "life-learnings": ("#3d1e08", "#7a3c10", "#b85a1a"),
}

def get_category(text):
    m = re.search(r'categories:\s*\n\s*-\s*(\S+)', text)
    return m.group(1) if m else "life-learnings"

def get_title(text):
    m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', text, re.M)
    return m.group(1) if m else "Post"

def get_emoji(text):
    m = re.search(r'cover:.*?image:\s*["\']?.*?(["\'])', text, re.S)
    cat = get_category(text)
    emojis = {
        "tech": ["💻","⚙️","🔧","📊","🖥️","🔌","📱","🌐","☁️","🧠"],
        "sanatana-dharma": ["🙏","🕉️","⭐","📿","🪔","✨","🔱","💫"],
        "temple-trails": ["🛕","🏛️","⛩️","🪷","🌸","🌺"],
        "shorts": ["💡","⚡","🎯","✍️","🌱","🔥"],
        "life-learnings": ["📖","🌟","🎓","🧭","💭","🌈"],
    }
    title = get_title(text).lower()
    elist = emojis.get(cat, emojis["life-learnings"])
    h = sum(ord(c) for c in title) % len(elist)
    return elist[h]

def make_svg(title, cat, emoji):
    dark, mid, light = PALETTES.get(cat, PALETTES["life-learnings"])
    short_title = title[:35] + "..." if len(title) > 35 else title
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{dark}"/>
      <stop offset="50%" style="stop-color:{mid}"/>
      <stop offset="100%" style="stop-color:{light}"/>
    </linearGradient>
    <pattern id="dots" width="30" height="30" patternUnits="userSpaceOnUse">
      <circle cx="15" cy="15" r="1" fill="rgba(255,255,255,0.08)"/>
    </pattern>
  </defs>
  <rect width="1200" height="630" fill="url(#bg)"/>
  <rect width="1200" height="630" fill="url(#dots)"/>
  <text x="600" y="280" text-anchor="middle" font-size="80" fill="white">{emoji}</text>
  <text x="600" y="400" text-anchor="middle" font-family="system-ui,sans-serif" font-weight="700" font-size="36" fill="white">{short_title}</text>
  <text x="600" y="445" text-anchor="middle" font-family="system-ui,sans-serif" font-weight="400" font-size="14" fill="rgba(255,255,255,0.6)" letter-spacing="3">BYTES &amp; BLESSINGS</text>
</svg>'''

count = 0
for md in sorted(posts.glob("*.md")):
    text = md.read_text(encoding="utf-8")
    title = get_title(text)
    cat = get_category(text)
    emoji = get_emoji(text)
    slug = md.stem
    svg_path = covers_dir / f"{slug}-cover.svg"
    svg_path.write_text(make_svg(title, cat, emoji), encoding="utf-8")
    img_path = f"/images/covers/{slug}-cover.svg"
    if "cover:" in text:
        text = re.sub(r'(cover:\s*\n\s*image:\s*).*', f'\\1"{img_path}"', text)
        text = re.sub(r'(relative:\s*)true', '\\1false', text)
    else:
        text = re.sub(
            r'(---\s*\n)',
            f'\\1cover:\n  image: "{img_path}"\n  relative: false\n  alt: "{title}"\n',
            text, count=1
        )
    md.write_text(text, encoding="utf-8")
    count += 1
    print(f"  {cat:20s} -> {slug}")

print(f"\nDone! Updated {count} covers with category-specific colors:")
print("  Tech        = Deep ocean blue")
print("  Awakened    = Royal indigo")
print("  Temple      = Rich purple")
print("  Sparks      = Emerald teal")
print("  Life        = Warm amber")
