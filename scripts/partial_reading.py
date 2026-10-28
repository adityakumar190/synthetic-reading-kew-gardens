
from pathlib import Path
import math

SOURCE = Path("corpus/story.txt")
OUTPUT = Path("partial_reading/partial_reading.txt")

PARTS = 2
SAMPLE_FRACTION = 0.20

text = SOURCE.read_text(encoding="utf-8")
original_lines = text.splitlines()

# Ignore blank lines for sampling but preserve original line numbers.
lines = [
    (i + 1, line)
    for i, line in enumerate(original_lines)
    if line.strip()
]

if not lines:
    raise ValueError("No nonblank lines found in corpus/story.txt")

# Split into two approximately equal sections.
part_size = math.ceil(len(lines) / PARTS)
selected = []

for part_index in range(PARTS):
    start = part_index * part_size
    end = min(start + part_size, len(lines))
    section = lines[start:end]

    if not section:
        continue

    count = max(1, math.ceil(len(section) * SAMPLE_FRACTION))
    sample = section[:count]
    selected.extend(sample)

    print(
        f"Part {part_index + 1}: "
        f"{len(section)} lines, selected {len(sample)}"
    )

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT.open("w", encoding="utf-8") as file:
    file.write("KEW GARDENS — PARTIAL READING\n")
    file.write("Method: first 20% of each of two sections\n\n")

    for line_number, line in selected:
        file.write(f"[Original line {line_number}] {line}\n")

print(f"Total nonblank lines: {len(lines)}")
print(f"Total selected lines: {len(selected)}")
print(f"Saved to {OUTPUT}")
