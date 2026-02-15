#!/usr/bin/env python3
"""Fix cover SVGs (XML entity) and frontmatter paths (remove leading /)"""
import re
from pathlib import Path

site = Path.home() / "Factory" / "BytesAndBlessings" / "site"
covers = site / "static" / "images" / "covers"
posts = site / "content" / "posts"

# Fix 1: SVG XML - escape & as &amp;
fixed_svg = 0
for svg in covers.glob("*.svg"):
    t = svg.read_text(encoding="utf-8")
    if "BYTES & BLESSINGS" in t:
        t = t.replace("BYTES & BLESSINGS", "BYTES &amp; BLESSINGS")
        svg.write_text(t, encoding="utf-8")
        fixed_svg += 1
print(f"1. Fixed {fixed_svg} SVGs (XML entity escape)")

# Fix 2: Remove leading / from cover image paths in frontmatter
fixed_md = 0
for md in posts.glob("*.md"):
    t = md.read_text(encoding="utf-8")
    if "image: \"/images/covers/" in t:
        t = t.replace("image: \"/images/covers/", "image: \"images/covers/")
        md.write_text(t, encoding="utf-8")
        fixed_md += 1
print(f"2. Fixed {fixed_md} posts (cover image paths)")
print("Done! Commit and push to deploy.")
