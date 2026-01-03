from typing import List, Dict, Any, Union, Optional
import uuid
import logging
from datetime import date
from .models import DataCenter, SubseaCable, GeoLocation, EntityStatus, ConfidenceLevel, Region

logger = logging.getLogger(__name__)

class NormalizationEngine:
    """
    Converts raw dictionary data into strict Pydantic models.
    Handles field mapping, validation, and defaults.
    """

    def normalize(self, raw_data: List[Dict[str, Any]]) -> List[Union[DataCenter, SubseaCable]]:
        normalized_items = []
        for item in raw_data:
            try:
                entity_type = item.get("type", "").lower()
                if entity_type == "datacenter":
                    normalized_items.append(self._normalize_datacenter(item))
                elif entity_type == "cable":
                    normalized_items.append(self._normalize_cable(item))
                else:
                    logger.warning(f"Unknown entity type: {entity_type}. Skipping.")
            except Exception as e:
                logger.error(f"Failed to normalize item '{item.get('name', 'UNKNOWN')}': {e}")
                
        return normalized_items

    def _generate_id(self, prefix: str, name: str) -> str:
        """Generates a deterministic-ish ID based on name."""
        # In a real system, we'd use a more robust hashing of unique attributes.
        clean_name = name.lower().replace(" ", "_").replace("-", "_")
        return f"{prefix}_{clean_name}_{uuid.uuid4().hex[:6]}"

    def _parse_region(self, region_str: str) -> Region:
        """Maps diverse region strings to our Enum."""
        # Simple mapping for MVP
        region_map = {
            "europe": Region.EU,
            "africa": Region.AF,
            "asia": Region.AS,
            "north america": Region.NA,
            "south america": Region.SA,
            "oceania": Region.OC,
            "middle east": Region.ME,
        }
        return region_map.get(region_str.lower(), Region.GLOBAL)

    def _parse_status(self, status_str: str) -> EntityStatus:
        try:
            return EntityStatus(status_str.lower())
        except ValueError:
            return EntityStatus.RUMORED # Default to lowest confidence if unknown

    def _normalize_location(self, loc_data: Dict[str, Any]) -> GeoLocation:
        return GeoLocation(
            latitude=loc_data.get("lat") or loc_data.get("latitude", 0.0),
            longitude=loc_data.get("lon") or loc_data.get("longitude", 0.0),
            country=loc_data.get("country", "Unknown"),
            city=loc_data.get("city"),
            region=self._parse_region(loc_data.get("region", ""))
        )

    def _normalize_datacenter(self, data: Dict[str, Any]) -> DataCenter:
        return DataCenter(
            id=data.get("id") or self._generate_id("dc", data["name"]),
            name=data["name"],
            owner_id=data.get("owner", "UNKNOWN_ORG"), # In real system, we'd resolve this to an Organization ID
            location=self._normalize_location(data["location"]),
            status=self._parse_status(data.get("status", "active")),
            source_urls=[data["source"]] if data.get("source") else [],
            notes=data.get("notes"),
            confidence=ConfidenceLevel.LIKELY # MVP default
        )

    def _normalize_cable(self, data: Dict[str, Any]) -> SubseaCable:
        # Handle date parsing
        rfs = None
        if data.get("rfs_date"):
            try:
                rfs = date.fromisoformat(data["rfs_date"])
            except ValueError:
                pass

        return SubseaCable(
            id=data.get("id") or self._generate_id("cable", data["name"]),
            name=data["name"],
            owners=data.get("owners", []),
            landing_points=[self._normalize_location(lp) for lp in data.get("landing_points", [])],
            status=self._parse_status(data.get("status", "active")),
            rfs_date=rfs,
            source_urls=[data["source"]] if data.get("source") else [],
            notes=data.get("notes"),
            confidence=ConfidenceLevel.LIKELY,
            geometry_coordinates=data.get("geometry_coordinates")
        )
