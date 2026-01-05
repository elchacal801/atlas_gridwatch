
import json
from pathlib import Path

INPUT_FILE = Path("data/processed/cloud_infrastructure_map.json")
OUTPUT_FILE = Path("docs/research/cloud_infrastructure_data.md")

def main():
    if not INPUT_FILE.exists():
        print("JSON file not found.")
        return

    data = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    
    md_lines = ["# Cloud Infrastructure Intelligence (OSINT)", ""]
    md_lines.append(f"**Source**: cloudinfrastructuremap.com (parsed raw text)")
    md_lines.append(f"**Total Assets**: {len(data)}")
    md_lines.append("")
    
    # Sort by Country -> City
    data.sort(key=lambda x: (x.get("location", {}).get("country", ""), x.get("location", {}).get("city", "")))
    
    current_country = None
    
    for item in data:
        loc = item.get("location", {})
        country = loc.get("country", "Unknown")
        city = loc.get("city", "Unknown")
        
        if country != current_country:
            md_lines.append(f"## {country}")
            current_country = country
        
        md_lines.append(f"- **{item.get('name')}** ({city})")
        md_lines.append(f"  - Owner: {item.get('owner')}")
        md_lines.append(f"  - Category: {item.get('category')}")
        if item.get("notes"):
            md_lines.append(f"  - Notes: {item.get('notes')}")
            
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Written Markdown to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
