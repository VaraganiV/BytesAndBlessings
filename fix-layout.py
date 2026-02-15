#!/usr/bin/env python3
"""Fix cover display: smaller SVGs + hide on post pages"""
import re
from pathlib import Path

site = Path.home() / "Factory" / "BytesAndBlessings" / "site"

# 1. Update hugo.yaml: hide cover on individual post pages
config = site / "hugo.yaml"
t = config.read_text(encoding="utf-8")
t = t.replace("hiddenInSingle: false", "hiddenInSingle: true")
config.write_text(t, encoding="utf-8")
print("1. Cover hidden on single post pages")

# 2. Regenerate all SVGs at 400px height with better proportions
covers = site / "static" / "images" / "covers"
count = 0
for svg_file in covers.glob("*.svg"):
    content = svg_file.read_text(encoding="utf-8")
    content = content.replace('height="630"', 'height="400"')
    content = content.replace('0 0 1200 630', '0 0 1200 400')
    content = content.replace('cy="15" r="1"', 'cy="15" r="0.8"')
    content = re.sub(r'font-size="80"', 'font-size="60"', content)
    content = re.sub(r'<text x="600" y="280"', '<text x="600" y="180"', content)
    content = re.sub(r'<text x="600" y="400"', '<text x="600" y="270"', content)
    content = re.sub(r'<text x="600" y="445"', '<text x="600" y="310"', content)
    svg_file.write_text(content, encoding="utf-8")
    count += 1

print(f"2. Resized {count} cover SVGs (630px -> 400px)")
print()
print("Result:")
print("  - Covers show on homepage listing (looks great)")
print("  - Covers hidden on individual post pages (clean reading)")
print("  - SVGs are shorter and more compact")
