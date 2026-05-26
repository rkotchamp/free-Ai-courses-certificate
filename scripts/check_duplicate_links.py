#!/usr/bin/env python3
"""Check README.md for duplicate markdown links."""
import re
from pathlib import Path

text = Path("README.md").read_text(encoding="utf-8")
links = re.findall(r"\[[^\]]+\]\((https?://[^)]+)\)", text)
seen = set()
dups = []
for link in links:
    normalized = link.rstrip("/").lower()
    if normalized in seen:
        dups.append(link)
    seen.add(normalized)

if dups:
    print("Duplicate links found:")
    for link in dups:
        print(f"- {link}")
    raise SystemExit(1)
print(f"OK: {len(links)} links checked, no duplicates found.")
