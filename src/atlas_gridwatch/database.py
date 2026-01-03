import json
import logging
from pathlib import Path
from typing import List, Dict, Any
from .models import DataCenter

logger = logging.getLogger(__name__)

class InfrastructureDatabase:
    """
    Manages persistence of infrastructure assets (Data Centers, Cables)
    to a JSON master file, handling deduplication and merging.
    """

    def __init__(self, db_path: Path = Path("data/processed/infrastructure_master.json")):
        self.db_path = db_path
        self.data: Dict[str, Dict] = {} # Keyed by ID
        self._load()

    def _load(self):
        """Loads existing data from JSON."""
        if not self.db_path.exists():
            self.data = {}
            return
        
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                raw_list = json.load(f)
                # Convert list back to dict keyed by ID for O(1) access
                for item in raw_list:
                    # Robustness: Handle if item is missing 'id'
                    oid = item.get('id')
                    if oid:
                        self.data[oid] = item
        except Exception as e:
            logger.error(f"Failed to load DB: {e}")
            self.data = {}

    def save(self):
        """Persists data to JSON."""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.db_path, 'w', encoding='utf-8') as f:
            # Sort by name for clean diffs
            sorted_list = sorted(list(self.data.values()), key=lambda x: x.get('name', ''))
            json.dump(sorted_list, f, indent=2)

    def upsert_asset(self, asset: DataCenter):
        """
        Inserts or Updates an asset. 
        Simple merge strategy: New overwrites old.
        """
        # Convert model to dict
        asset_dict = asset.model_dump(mode='json')
        self.data[asset.id] = asset_dict
        
    def bulk_upsert(self, assets: List[DataCenter]):
        for a in assets:
            self.upsert_asset(a)
        self.save()

    def get_all(self) -> List[Dict]:
        return list(self.data.values())
