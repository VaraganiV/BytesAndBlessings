#!/usr/bin/env python3
from pathlib import Path
config = Path.home() / "Factory" / "BytesAndBlessings" / "site" / "hugo.yaml"
text = config.read_text(encoding="utf-8")
marker = "# Main menu"
idx = text.find(marker)
if idx == -1:
    print("ERROR: Could not find '# Main menu' in hugo.yaml")
    exit(1)
before = text[:idx]
new_menu = """# Main menu
menu:
  main:
    - identifier: tech
      name: "Tech"
      url: /categories/tech/
      weight: 10
    - identifier: awakened
      name: "Awakened"
      url: /categories/sanatana-dharma/
      weight: 20
    - identifier: temple-trails
      name: "Temple Trails"
      url: /categories/temple-trails/
      weight: 30
    - identifier: sparks
      name: "Sparks"
      url: /categories/shorts/
      weight: 40
    - identifier: tags
      name: "Tags"
      url: /tags/
      weight: 50
    - identifier: search
      name: "Search"
      url: /search/
      weight: 60
    - identifier: about
      name: "About"
      url: /about/
      weight: 70
"""
config.write_text(before + new_menu, encoding="utf-8")
print("Menu updated!")
final = config.read_text(encoding="utf-8")
for line in final.split("\n"):
    if "name:" in line and "weight" not in line and "Title" not in line:
        print("  " + line.strip())
