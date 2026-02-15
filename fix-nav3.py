#!/usr/bin/env python3
from pathlib import Path
config = Path.home() / "Factory" / "BytesAndBlessings" / "site" / "hugo.yaml"
text = config.read_text(encoding="utf-8")
lines = text.split("\n")
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if "Shorts" in line and "name:" in line:
        new_lines.append('      name: "Sparks"')
        i += 1
        continue
    if "identifier: shorts" in line:
        new_lines.append('    - identifier: sparks')
        i += 1
        continue
    if "identifier: search" in line:
        new_lines.append("    - identifier: tags")
        new_lines.append('      name: "Tags"')
        new_lines.append("      url: /tags/")
        new_lines.append("      weight: 50")
        new_lines.append(line.replace("weight: 50", "weight: 60").replace("weight: 40", "weight: 60"))
        i += 1
        continue
    if "identifier: about" in line:
        new_lines.append(line)
        i += 1
        if i < len(lines) and "name:" in lines[i]:
            new_lines.append(lines[i])
            i += 1
        if i < len(lines) and "url:" in lines[i]:
            new_lines.append(lines[i])
            i += 1
        if i < len(lines) and "weight:" in lines[i]:
            new_lines.append("      weight: 70")
            i += 1
        continue
    new_lines.append(line)
    i += 1
config.write_text("\n".join(new_lines), encoding="utf-8")
print("Done! Updated menu:")
for l in new_lines:
    if "name:" in l and "weight" not in l and ("Tech" in l or "Awaken" in l or "Temple" in l or "Spark" in l or "Tag" in l or "Search" in l or "About" in l):
        print("  " + l.strip())
