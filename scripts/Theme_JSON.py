"""Theme analysis for Virginia Woolf's Kew Gardens."""

import json
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "themes.json"

with INPUT_FILE.open(encoding="utf-8") as file:
    data = json.load(file)

annotations = data["annotations"]

primary_counts = Counter(
    item["primary_theme"] for item in annotations
)

all_counts = Counter()
for item in annotations:
    all_counts[item["primary_theme"]] += 1
    all_counts.update(item.get("secondary_themes", []))

print("Work:", data["work"]["title"])
print("Author:", data["work"]["author"])
print("Total annotations:", len(annotations))

print("\\nPrimary theme counts:")
for theme, count in primary_counts.most_common():
    print(f"{theme}: {count}")

print("\\nAll theme assignments (primary + secondary):")
for theme, count in all_counts.most_common():
    print(f"{theme}: {count}")
