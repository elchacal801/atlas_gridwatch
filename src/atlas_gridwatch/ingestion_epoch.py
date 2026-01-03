import csv
import re
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

class EpochIngestor:
    """
    Ingests data from Epoch AI's 'Frontier Data Centers' CSV.
    Handles legacy coordinate formats (DMS) and cleans owner fields.
    """

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def _dms_to_decimal(self, dms_str: str) -> float:
        """
        Parses strings like '32A35'25""N' or '32°35'25"N' into decimal degrees.
        """
        if not dms_str or not isinstance(dms_str, str):
            return 0.0
            
        # Clean artifacts like A 
        clean_str = dms_str.replace("A", "°").replace('""', '"').strip()
        
        # Regex for DMS
        # Matches: 32°35'25"N
        match = re.match(r"(\d+)°(\d+)'([\d\.]+)\"?([NSEW])", clean_str)
        if not match:
            # Fallback for simple decimal if exists
            try:
                return float(clean_str)
            except:
                return 0.0

        deg, minutes, seconds, direction = match.groups()
        decimal = float(deg) + float(minutes)/60 + float(seconds)/3600
        
        if direction in ['S', 'W']:
            decimal = -decimal
            
        return decimal

    def fetch(self) -> List[Dict[str, Any]]:
        results = []
        if not self.file_path.exists():
            logger.error(f"Epoch file not found: {self.file_path}")
            return results

        try:
            with open(self.file_path, 'r', encoding='utf-8', errors='replace') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Parse Coordinates
                    lat = self._dms_to_decimal(row.get("Latitude"))
                    lon = self._dms_to_decimal(row.get("Longitude"))
                    
                    if lat == 0.0 and lon == 0.0:
                        continue # Skip invalid location
                    
                    # Clean Owner (remove #tags)
                    raw_owner = row.get("Owner", "Unknown")
                    owner = raw_owner.split("#")[0].strip() if raw_owner else "Unknown"
                    if not owner: owner = "Unknown"

                    # Status - infer from columns or default
                    # Epoch tracks 'timelines', if 'Current power' > 0 it's likely active or close
                    mw = row.get("Current power (MW)", "0")
                    status = "active" if float(mw) > 0 else "planned"

                    results.append({
                        "type": "datacenter", # Fix: Required for normalization
                        "name": row.get("Title") or row.get("Project") or "Unnamed Epoch Facility",
                        "owner_id": owner,
                        "location": {
                            "city": row.get("Address", "Unknown").split(",")[0], # Rough city extract
                            "country": "Unknown", # Epoch data implies US usually but not always?
                            "region": "Global",
                            "latitude": lat,
                            "longitude": lon
                        },
                        "status": status,
                        "properties": {
                            "power_mw": mw,
                            "h100_equiv": row.get("Current H100 equivalents"),
                            "source": "Epoch AI"
                        }
                    })

        except Exception as e:
            logger.error(f"Epoch Ingestion failed: {e}")
        
        return results
