
import sys
from pathlib import Path
import csv

# Mocking the paths used in generate_brief.py
base_dir = Path.cwd()
print(f"Current Working Directory: {base_dir}")

nodes_path = base_dir / "data/outputs/critical_nodes.csv"
ai_path = base_dir / "data/outputs/ai_assessment.html"

print(f"Checking {nodes_path}...")
if nodes_path.exists():
    print(f"  Exists. Size: {nodes_path.stat().st_size} bytes")
    try:
        with open(nodes_path, 'r', encoding='utf-8') as f:
            data = list(csv.DictReader(f))
        print(f"  Loaded {len(data)} rows.")
        if len(data) > 0:
            print(f"  First row: {data[0]}")
    except Exception as e:
        print(f"  Error reading CSV: {e}")
else:
    print(f"  Does NOT exist.")

print(f"Checking {ai_path}...")
if ai_path.exists():
    print(f"  Exists. Size: {ai_path.stat().st_size} bytes")
    try:
        content = ai_path.read_text(encoding="utf-8")
        print(f"  Content length: {len(content)}")
    except Exception as e:
        print(f"  Error reading text: {e}")
else:
    print(f"  Does NOT exist.")
