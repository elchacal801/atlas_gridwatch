
import json
import re
from typing import List, Dict, Any
from pathlib import Path

# --- CONFIG ---
INPUT_FILE = Path("data/raw/cloud_infrastructure_map_raw.txt")
OUTPUT_FILE = Path("data/processed/cloud_infrastructure_map.json")

# --- GEOCODING DB (Embedded for Reliability) ---
CITY_COORDS = {
    "buenos aires": {"lat": -34.6037, "lon": -58.3816},
    "canberra": {"lat": -35.2809, "lon": 149.1300},
    "melbourne": {"lat": -37.8136, "lon": 144.9631},
    "sydney": {"lat": -33.8688, "lon": 151.2093},
    "vienna": {"lat": 48.2082, "lon": 16.3738},
    "manama": {"lat": 26.2277, "lon": 50.5860},
    "brussels": {"lat": 50.8503, "lon": 4.3517},
    "mons": {"lat": 50.4542, "lon": 3.9567},
    "campinas": {"lat": -22.9099, "lon": -47.0626},
    "rio de janeiro": {"lat": -22.9068, "lon": -43.1729},
    "são paulo": {"lat": -23.5505, "lon": -46.6333},
    "sap paulo": {"lat": -23.5505, "lon": -46.6333},
    "santana de parnaiba": {"lat": -23.4442, "lon": -46.9205},
    "calgary": {"lat": 51.0447, "lon": -114.0719},
    "montréal": {"lat": 45.5017, "lon": -73.5673},
    "montreal": {"lat": 45.5017, "lon": -73.5673},
    "quebec city": {"lat": 46.8139, "lon": -71.2080},
    "toronto": {"lat": 43.6532, "lon": -79.3832},
    "vancouver": {"lat": 49.2827, "lon": -123.1207},
    "santiago": {"lat": -33.4489, "lon": -70.6693},
    "valparaíso": {"lat": -33.0472, "lon": -71.6127},
    "beijing": {"lat": 39.9042, "lon": 116.4074},
    "chengdu": {"lat": 30.5728, "lon": 104.0668},
    "chongqing": {"lat": 29.5630, "lon": 106.5516},
    "fuzhou": {"lat": 26.0745, "lon": 119.2965},
    "guangzhou": {"lat": 23.1291, "lon": 113.2644},
    "guiyang": {"lat": 26.6420, "lon": 106.6300},
    "hangzhou": {"lat": 30.2741, "lon": 120.1551},
    "heyuan": {"lat": 23.7290, "lon": 114.6975},
    "hong kong": {"lat": 22.3193, "lon": 114.1694},
    "huhehaote": {"lat": 40.8419, "lon": 111.7488},
    "hohhot": {"lat": 40.8419, "lon": 111.7488},
    "karamay": {"lat": 45.5798, "lon": 84.8893},
    "nanjing": {"lat": 32.0603, "lon": 118.7969},
    "ningxiang": {"lat": 28.2532, "lon": 112.5583},
    "qingdao": {"lat": 36.0671, "lon": 120.3826},
    "shanghai": {"lat": 31.2304, "lon": 121.4737},
    "shenzhen": {"lat": 22.5431, "lon": 114.0579},
    "ulanqab": {"lat": 41.0188, "lon": 113.1118},
    "wuhan": {"lat": 30.5928, "lon": 114.3055},
    "wuhu": {"lat": 31.3524, "lon": 118.4326},
    "zhangjiakou": {"lat": 40.8105, "lon": 114.8863},
    "bogotá": {"lat": 4.7110, "lon": -74.0721},
    "bogota": {"lat": 4.7110, "lon": -74.0721},
    "copenhagen": {"lat": 55.6761, "lon": 12.5683},
    "cairo": {"lat": 30.0444, "lon": 31.2357},
    "hamina": {"lat": 60.5693, "lon": 27.1983},
    "helsinki": {"lat": 60.1695, "lon": 24.9354},
    "dunkerque": {"lat": 51.0543, "lon": 2.3738},
    "lille": {"lat": 50.6292, "lon": 3.0573},
    "marseille": {"lat": 43.2965, "lon": 5.3698},
    "paris": {"lat": 48.8566, "lon": 2.3522},
    "strasbourg": {"lat": 48.5734, "lon": 7.7521},
    "berlin": {"lat": 52.5200, "lon": 13.4050},
    "frankfurt": {"lat": 50.1109, "lon": 8.6821},
    "hamburg": {"lat": 53.5511, "lon": 9.9937},
    "munich": {"lat": 48.1351, "lon": 11.5820},
    "düsseldorf": {"lat": 51.2277, "lon": 6.7735},
    "athens": {"lat": 37.9838, "lon": 23.7275},
    "chennai": {"lat": 13.0827, "lon": 80.2707},
    "hyderabad": {"lat": 17.3850, "lon": 78.4867},
    "mumbai": {"lat": 19.0760, "lon": 72.8777},
    "new delhi": {"lat": 28.6139, "lon": 77.2090},
    "pune": {"lat": 18.5204, "lon": 73.8567},
    "bangalore": {"lat": 12.9716, "lon": 77.5946},
    "kolkata": {"lat": 22.5726, "lon": 88.3639},
    "batam": {"lat": 1.1301, "lon": 104.0529},
    "jakarta": {"lat": -6.2088, "lon": 106.8456},
    "dublin": {"lat": 53.3498, "lon": -6.2603},
    "jerusalem": {"lat": 31.7683, "lon": 35.2137},
    "tel aviv": {"lat": 32.0853, "lon": 34.7818},
    "haifa": {"lat": 32.7940, "lon": 34.9896},
    "milan": {"lat": 45.4642, "lon": 9.1900},
    "turin": {"lat": 45.0703, "lon": 7.6869},
    "osaka": {"lat": 34.6937, "lon": 135.5023},
    "tokyo": {"lat": 35.6762, "lon": 139.6503},
    "nairobi": {"lat": -1.2921, "lon": 36.8219},
    "kuala lumpur": {"lat": 3.1390, "lon": 101.6869},
    "mexico city": {"lat": 19.4326, "lon": -99.1332},
    "monterrey": {"lat": 25.6866, "lon": -100.3161},
    "santiago de querétaro": {"lat": 20.5888, "lon": -100.3899},
    "querétaro": {"lat": 20.5888, "lon": -100.3899},
    "casablanca": {"lat": 33.5731, "lon": -7.5898},
    "rabat": {"lat": 34.0209, "lon": -6.8416},
    "settat": {"lat": 33.0010, "lon": -7.6166},
    "amsterdam": {"lat": 52.3676, "lon": 4.9041},
    "groningen": {"lat": 53.2194, "lon": 6.5665},
    "auckland": {"lat": -36.8485, "lon": 174.7633},
    "oslo": {"lat": 59.9139, "lon": 10.7522},
    "stavanger": {"lat": 58.9690, "lon": 5.7331},
    "lima": {"lat": -12.0464, "lon": -77.0428},
    "manila": {"lat": 14.5995, "lon": 120.9842},
    "sochaczew": {"lat": 52.2263, "lon": 20.2372},
    "warsaw": {"lat": 52.2297, "lon": 21.0122},
    "doha": {"lat": 25.2854, "lon": 51.5310},
    "muscat": {"lat": 23.5880, "lon": 58.3829},
    "dammam": {"lat": 26.4207, "lon": 50.0888},
    "jeddah": {"lat": 21.4858, "lon": 39.1925},
    "riyadh": {"lat": 24.7136, "lon": 46.6753},
    "kragujevac": {"lat": 44.0128, "lon": 20.9114},
    "singapore": {"lat": 1.3521, "lon": 103.8198},
    "cape town": {"lat": -33.9249, "lon": 18.4241},
    "johannesburg": {"lat": -26.2041, "lon": 28.0473},
    "busan": {"lat": 35.1796, "lon": 129.0756},
    "chuncheon": {"lat": 37.8813, "lon": 127.7298},
    "seoul": {"lat": 37.5665, "lon": 126.9780},
    "madrid": {"lat": 40.4168, "lon": -3.7038},
    "zaragoza": {"lat": 41.6488, "lon": -0.8891},
    "gävle": {"lat": 60.6749, "lon": 17.1412},
    "malmö": {"lat": 55.6045, "lon": 13.0038},
    "stockholm": {"lat": 59.3293, "lon": 18.0686},
    "geneva": {"lat": 46.2044, "lon": 6.1432},
    "zürich": {"lat": 47.3769, "lon": 8.5417},
    "taichung": {"lat": 24.1477, "lon": 120.6736},
    "taipei": {"lat": 25.0330, "lon": 121.5654},
    "bangkok": {"lat": 13.7563, "lon": 100.5018},
    "istanbul": {"lat": 41.0082, "lon": 28.9784},
    "abu dhabi": {"lat": 24.4539, "lon": 54.3773},
    "dubai": {"lat": 25.2048, "lon": 55.2708},
    "cardiff": {"lat": 51.4816, "lon": -3.1791},
    "london": {"lat": 51.5074, "lon": -0.1278},
    "newport": {"lat": 51.5842, "lon": -2.9977},
    "manchester": {"lat": 53.4808, "lon": -2.2426},
    "atlanta": {"lat": 33.7490, "lon": -84.3880},
    "austin": {"lat": 30.2672, "lon": -97.7431},
    "charleston": {"lat": 32.7765, "lon": -79.9311},
    "cheyenne": {"lat": 41.1400, "lon": -104.8202},
    "chicago": {"lat": 41.8781, "lon": -87.6298},
    "columbus": {"lat": 39.9612, "lon": -82.9988},
    "dallas": {"lat": 32.7767, "lon": -96.7970},
    "des moines": {"lat": 41.5868, "lon": -93.6250},
    "hermiston": {"lat": 45.8432, "lon": -119.2895},
    "las vegas": {"lat": 36.1699, "lon": -115.1398},
    "los angeles": {"lat": 34.0522, "lon": -118.2437},
    "moses lake": {"lat": 47.1301, "lon": -119.2781},
    "omaha": {"lat": 41.2565, "lon": -95.9345},
    "phoenix": {"lat": 33.4484, "lon": -112.0740},
    "portland": {"lat": 45.5152, "lon": -122.6784},
    "richmond": {"lat": 37.5407, "lon": -77.4360},
    "salt lake city": {"lat": 40.7608, "lon": -111.8910},
    "san antonio": {"lat": 29.4241, "lon": -98.4936},
    "san francisco": {"lat": 37.7749, "lon": -122.4194},
    "the dalles": {"lat": 45.6018, "lon": -121.1823},
    "washington": {"lat": 38.9072, "lon": -77.0369},
    "boston": {"lat": 42.3601, "lon": -71.0589},
    "denver": {"lat": 39.7392, "lon": -104.9903},
    "fresno": {"lat": 36.7378, "lon": -119.7871},
    "honolulu": {"lat": 21.3069, "lon": -157.8583},
    "houston": {"lat": 29.7604, "lon": -95.3698},
    "kansas city": {"lat": 39.0997, "lon": -94.5786},
    "miami": {"lat": 25.7617, "lon": -80.1918},
    "minneapolis": {"lat": 44.9778, "lon": -93.2650},
    "new york": {"lat": 40.7128, "lon": -74.0060},
    "philadelphia": {"lat": 39.9526, "lon": -75.1652},
    "seattle": {"lat": 47.6062, "lon": -122.3321},
    "st. louis": {"lat": 38.6270, "lon": -90.1994},
    "hanoi": {"lat": 21.0285, "lon": 105.8542},
    "ho chi minh city": {"lat": 10.8231, "lon": 106.6297},
    "sofia": {"lat": 42.6977, "lon": 23.3219},
    "abidjan": {"lat": 5.3097, "lon": -4.0127},
    "prague": {"lat": 50.0755, "lon": 14.4378},
    "lagos": {"lat": 6.5244, "lon": 3.3792},
    "lisbon": {"lat": 38.7223, "lon": -9.1393},
    "buacharest": {"lat": 44.4268, "lon": 26.1025},
    "bucharest": {"lat": 44.4268, "lon": 26.1025},
    "luxembourg": {"lat": 49.6116, "lon": 6.1319},
    "tunis": {"lat": 36.8065, "lon": 10.1815}
}

def get_coords(city_name: str, country_name: str) -> Dict[str, float]:
    key = city_name.lower().strip()
    if key in CITY_COORDS:
        return CITY_COORDS[key]
    # Fallback to Country Center usually? No, better default to 0,0 or handle gracefully
    # For now, return 0,0
    return {"lat": 0.0, "lon": 0.0}

def parse_txt():
    if not INPUT_FILE.exists():
        print(f"Error: {INPUT_FILE} not found.")
        return

    text = INPUT_FILE.read_text(encoding="utf-8")
    lines = [L.strip() for L in text.splitlines() if L.strip()]
    
    results = []
    
    # State Machine
    # Modes: "REGIONS", "LOCAL_ZONES", "ON_RAMPS"
    mode = None
    
    # Headers
    # "Cloud Regions" -> "Metro Area", "Country", "Provider info..."
    # "Local Zones" -> "Metro Area", "Country", "Zone info..."
    # "On-Ramps" -> "Metro Area", "Country", "Ramp info..."
    
    # Simple iteration
    # Since the file structure is irregular blocks (Metro Line, Country Line, Multiple Item Lines),
    # we need to detect Metro/Country pairs.
    # The header sections divide the file.
    
    # Strategy: Split by Section Headers first
    
    # Find indices
    idx_regions = -1
    idx_zones = -1
    idx_ramps = -1
    
    for i, line in enumerate(lines):
        if line == "Cloud Regions": idx_regions = i
        elif line == "Local Zones": idx_zones = i
        elif line == "On-Ramps": idx_ramps = i

    # Define content blocks
    # Assume order: Regions, Local Zones, On-Ramps
    # But check indices to be sure
    sections = []
    if idx_regions != -1: sections.append((idx_regions, "REGIONS"))
    if idx_zones != -1: sections.append((idx_zones, "LOCAL_ZONES"))
    if idx_ramps != -1: sections.append((idx_ramps, "ON_RAMPS"))
    
    sections.sort()
    
    for k in range(len(sections)):
        start_idx, section_type = sections[k]
        end_idx = sections[k+1][0] if k < len(sections)-1 else len(lines)
        
        # Process block
        block_lines = lines[start_idx+1 : end_idx]
        process_section(block_lines, section_type, results)

    # Save
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    
    print(f"Successfully parsed {len(results)} items to {OUTPUT_FILE}")

def process_section(lines, section_type, results):
    # Removing header artifacts like "Metro Area", "Cloud Service Provider..."
    # They usually appear at the start
    
    # Heuristic:
    # A Metro area is usually a City Name (no commas usually)
    # Followed by Country Name
    # Followed by 1 or more lines containing commas (Data)
    
    i = 0
    current_metro = None
    current_country = None
    
    while i < len(lines):
        line = lines[i]
        
        # Skip header noise
        if line in ["Metro Area", "Cloud Service Provider, Cloud Region", "Zone Name, Parent Region, Access Facility", "Cloud Service Provider, Data Center, Data Center Operator"]:
            i += 1
            continue
            
        # Check if this line looks like a Metro (Single word or few words, no commas usually, unless "Washington, D.C.")
        # But data lines HAVE commas. Metro/Country usually don't (except rare cases).
        # Data lines usually have "Provider," starts with provider name.
        
        # Weak heuristic: If line has comma, it's DATA.
        # If line has NO comma, it's METRO or COUNTRY.
        
        if "," in line:
            # It's a data line, associated with current_metro/country
            if current_metro and current_country:
                parse_item(line, current_metro, current_country, section_type, results, lines, i)
            i += 1
        else:
            # It is likely Metro or Country
            # Expect Metro then Country
            # Look ahead
            if i + 1 < len(lines):
                next_line = lines[i+1]
                if "," not in next_line:
                    # Found a Pair: Metro / Country
                    current_metro = line
                    current_country = next_line
                    i += 2
                else:
                    # Valid case: Metro might be "Washington, D.C." (has comma)
                    # But if we treat comma as data separator, we fail.
                    # Adjust header check: Cloud providers are specific.
                    # Or check if next line is Country which is usually known?
                    # Let's assume standard format: City \n Country
                    
                    # If single line without comma, treat as Metro (if curr_country set) -> New Metro?
                    # Actually, raw text has strictly:
                    # City
                    # Country
                    # Item
                    # Item
                    
                    # So if we see two non-comma lines consecutively, update Metro/Country.
                    i += 1
            else:
                 i += 1

def parse_item(line, city, country, section_type, results, all_lines, current_idx):
    # item parsing based on section
    # REGIONS: "Provider, Region Name Zones" ...
    # ZONES: "Provider, Zone Name, Parent, Status"
    # RAMPS: "Provider, DC Name, Operator" \n "Address" (Sometimes address is next line)
    
    coords = get_coords(city, country)
    
    if section_type == "REGIONS":
        parts = line.split(",", 1)
        if len(parts) < 2: return
        provider = parts[0].strip()
        details = parts[1].strip()
        
        results.append({
            "type": "datacenter",
            "name": f"{provider} - {city} Region",
            "owner": provider,
            "location": {
                "city": city,
                "country": country,
                "lat": coords["lat"],
                "lon": coords["lon"],
                "region": "Global"
            },
            "status": "active", # Default
            "source": "https://www.cloudinfrastructuremap.com/",
            "notes": details,
            "category": "Cloud Region"
        })
        
    elif section_type == "LOCAL_ZONES":
        parts = line.split(",")
        provider = parts[0].strip()
        # Varies
        results.append({
            "type": "datacenter",
            "name": f"{provider} - {city} Local Zone",
            "owner": provider,
            "location": {
                "city": city,
                "country": country,
                "lat": coords["lat"],
                "lon": coords["lon"],
                 "region": "Global"
            },
            "status": "active",
            "source": "https://www.cloudinfrastructuremap.com/",
            "notes": line,
            "category": "Local Zone"
        })

    elif section_type == "ON_RAMPS":
        # Check for address in next line
        # Line: "Amazon Web Services, Cirion BUE1, Cirion"
        # Next Line: "Avenue del Campo 1301, Buenos Aires, Argentina" (Has numbers, usually)
        # But next line could be next item (if it starts with Provider).
        
        # Check next line
        address = ""
        if current_idx + 1 < len(all_lines):
            nxt = all_lines[current_idx+1]
            # Heuristic: If next line has no known provider at start?
            # Or if it looks like address.
            # Most addresses have numbers.
            # "Alibaba Cloud" is provider.
            # If next line starts with a provider name, it's a new item.
            
            providers = ["Alibaba", "Amazon", "Google", "Huawei", "IBM", "Microsoft", "Oracle", "Tencent", "OVH"]
            is_provider = any(nxt.startswith(p) for p in providers)
            
            if not is_provider and "," in nxt:
                # Likely address
                address = nxt
                # Consume it? No, loop iterator handles i. BUT we are called from process_section which increments i by 1.
                # Use a hack? process_section should handle skipping address lines if consume here.
                # Actually process_section logic: "if ',' in line: parse_item".
                # If address has comma, it triggers parse_item.
                # Address usually doesn't start with Provider.
                # So we can just attach address to previous item if it lacks provider?
                pass

        parts = line.split(",")
        provider = parts[0].strip()
        dc_name = parts[1].strip() if len(parts) > 1 else "Unknown DC"
        
        results.append({
            "type": "datacenter",
            "name": f"{provider} On-Ramp - {dc_name}",
            "owner": provider,
            "location": {
                "city": city,
                "country": country,
                "lat": coords["lat"],
                "lon": coords["lon"],
                 "region": "Global"
            },
            "status": "active",
            "source": "https://www.cloudinfrastructuremap.com/",
            "notes": f"On-Ramp. {line}",
            "category": "On-Ramp"
        })

if __name__ == "__main__":
    parse_txt()
