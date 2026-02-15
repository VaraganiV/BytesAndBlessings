#!/usr/bin/env python3
import os, re
from pathlib import Path
SITE=Path(os.path.expanduser("~/Factory/BytesAndBlessings/site"))
POSTS=SITE/"content"/"posts"
COVERS=SITE/"static"/"images"/"covers"
COVERS.mkdir(parents=True, exist_ok=True)

for svg in POSTS.glob("*-cover.svg"):
    dest=COVERS/svg.name
    dest.write_text(svg.read_text())
    svg.unlink()
    print(f"Moved: {svg.name}")

for md in POSTS.glob("*.md"):
    c=md.read_text(encoding='utf-8')
    if '-cover.svg' not in c: continue
    c=c.replace('  relative: true','  relative: false')
    c=re.sub(r'image: "([^"]*-cover\.svg)"', r'image: "/images/covers/\1"', c)
    md.write_text(c, encoding='utf-8')
    print(f"Fixed: {md.name}")

print("\nDone!")
