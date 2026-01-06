import json
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Union
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class BaseIngestor(ABC):
    """Abstract base class for all data ingestors."""

    @abstractmethod
    def fetch(self) -> List[Dict[str, Any]]:
        """
        Fetch data from the source.
        Returns a list of raw dictionaries containing the data.
        """
        pass

class FileIngestor(BaseIngestor):
    """Ingests data from a local JSON file."""

    def __init__(self, file_path: Union[str, Path]):
        self.file_path = Path(file_path)

    def fetch(self) -> List[Dict[str, Any]]:
        if not self.file_path.exists():
            logger.error(f"File not found: {self.file_path}")
            return []
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                elif isinstance(data, dict):
                     # Wrap single object or dict-based structure if needed, 
                     # but for now assume list of items
                     return [data]
                else:
                    logger.warning(f"Unexpected data format in {self.file_path}. Expected list or dict.")
                    return []
        except json.JSONDecodeError as e:
            logger.error(f"Failed to decode JSON from {self.file_path}: {e}")
            return []
        except Exception as e:
            logger.error(f"Error reading file {self.file_path}: {e}")
            return []

class SeedDataIngestor(BaseIngestor):
    """Ingests hardcoded seed data for testing purposes."""

    def fetch(self) -> List[Dict[str, Any]]:
        # This returns raw dictionary structure matching the seed definition
        return [
             {
                "type": "datacenter",
                "name": "Marseille MRS2",
                "owner": "Interxion",
                "location": {
                    "lat": 43.3, 
                    "lon": 5.4, 
                    "country": "France",
                    "city": "Marseille",
                    "region": "Europe"
                },
                "status": "active",
                "source": "https://www.interxion.com/locations/europe/france/marseille/mrs2",
                "notes": "Key landing hub for subsea cables from Africa and Asia."
            },
            {
                "type": "cable",
                "name": "2Africa",
                "owners": ["Meta", "Vodafone", "MTN", "Orange", "China Mobile"],
                "landing_points": [
                     {"lat": 43.3, "lon": 5.4, "country": "France", "region": "Europe"},
                     {"lat": -33.9, "lon": 18.4, "country": "South Africa", "region": "Africa"}
                ],
                "status": "under_construction",
                "rfs_date": "2024-01-01",
                "source": "https://www.2africacable.net",
                "notes": "One of the longest cable systems in the world."
            }
        ]

import requests

class TeleGeographyIngestor(BaseIngestor):
    """Ingests data from the TeleGeography Submarine Cable Map public API."""
    
    def fetch(self) -> List[Dict[str, Any]]:
        logger.info(f"Fetching data from TeleGeography...")
        try:
            # 1. Fetch Metadata Summary (to get IDs)
            summary_url = "https://www.submarinecablemap.com/api/v3/cable/all.json"
            headers = {"User-Agent": "AtlasGridwatch/1.0 (Research Project)"}
            resp_summary = requests.get(summary_url, headers=headers, timeout=15)
            resp_summary.raise_for_status()
            summary_list = resp_summary.json()
            
            # 2. Fetch Geometry (Bulk)
            geo_url = "https://www.submarinecablemap.com/api/v3/cable/cable-geo.json"
            resp_geo = requests.get(geo_url, headers=headers, timeout=30)
            resp_geo.raise_for_status()
            geo_data = resp_geo.json()
            
            # Index Geometry by ID
            geo_map = {}
            for feature in geo_data.get("features", []):
                fid = feature.get("properties", {}).get("id")
                geo_map[fid] = feature.get("geometry", {}).get("coordinates", [])

            # 3. Process Top 50 Cables (Fetch details for Owners)
            results = []
            target_cables = summary_list # Fetch complete list
            
            logger.info(f"Fetching details for {len(target_cables)} cables... (This may take a few minutes)")
            
            for i, item in enumerate(target_cables):
                cid = item.get("id")
                
                # Fetch Detail
                detail_url = f"https://www.submarinecablemap.com/api/v3/cable/{cid}.json"
                try:
                    if i > 0: import time; time.sleep(0.05)
                    resp_detail = requests.get(detail_url, headers=headers, timeout=5)
                    if resp_detail.status_code != 200: continue
                    detail = resp_detail.json()
                    
                    # Extract Geometry if available in Bulk map
                    resampled_coords = []
                    if cid in geo_map:
                        raw_coords = geo_map[cid]
                        # Convert GeoJSON [lon, lat] -> Folium [lat, lon]
                        # Handle MultiLineString structure
                        # Structure is usually [ [ [lon, lat], ... ] ]
                        # We need to be careful with nesting.
                        # Recursively find lists of points?
                        # Let's assume standard MultiLineString: List of List of Points.
                        
                        def flip_coords(coords):
                            if not coords: return []
                            # If it's a point [lon, lat] (len 2 float)
                            if len(coords) == 2 and isinstance(coords[0], (int, float)):
                                return [coords[1], coords[0]]
                            # Else recurse
                            return [flip_coords(c) for c in coords]

                        # The logic above is recursive generic. 
                        # cable-geo.json usually: [ [ [x,y], [x,y] ], [ [x,y] ] ]
                        # We want: [ [ [y,x], [y,x] ], ... ]
                        resampled_coords = flip_coords(raw_coords)
                    
                    owners_data = detail.get("owners")
                    owners_list = []
                    if isinstance(owners_data, str):
                        owners_list = [o.strip() for o in owners_data.split(",")]
                    elif isinstance(owners_data, list):
                        owners_list = [o.get("name", str(o)) if isinstance(o, dict) else str(o) for o in owners_data]
                    
                    # Parse Landing Points for Analysis (Graph Topology)
                    # Even if we don't have coords, we need them for Network Analysis
                    lps_list = detail.get("landing_points", [])
                    # The NormalizationEngine expects "lat", "lon" or "latitude", "longitude" or relies on defaults (0,0)
                    # We pass the raw dicts, Analysis uses 'country' and 'name'.

                    results.append({
                        "type": "cable",
                        "id": str(cid),
                        "name": detail.get("name"),
                        "owners": owners_list,
                        "rfs_date": detail.get("rfs"),
                        "source": detail_url,
                        "status": "active" if detail.get("is_active") else "planned",
                        "geometry_coordinates": resampled_coords,
                        "landing_points": lps_list 
                    })
                    
                except Exception as ex:
                    logger.warning(f"Failed to fetch details for {cid}: {ex}")
                    continue

            return results

        except Exception as e:
            logger.error(f"Failed to fetch from TeleGeography: {e}")
            return []
