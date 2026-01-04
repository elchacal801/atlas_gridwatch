from datetime import date
from enum import Enum
from typing import List, Optional, Literal
from pydantic import BaseModel, Field, HttpUrl

# --- Enums for Standardization ---

class EntityStatus(str, Enum):
    ACTIVE = "active"
    PLANNED = "planned"
    UNDER_CONSTRUCTION = "under_construction"
    DECOMMISSIONED = "decommissioned"
    RUMORED = "rumored"

class ConfidenceLevel(str, Enum):
    CONFIRMED = "confirmed"  # Verified by multiple independent sources or official announcement
    LIKELY = "likely"        # High probability based on strong indicators
    CLAIMED = "claimed"      # Stated by a single source without independent verification
    DISPUTED = "disputed"    # Conflicting reports exist
    LOW = "low"              # Inferred with weak evidence

class Region(str, Enum):
    NA = "North America"
    SA = "South America"
    EU = "Europe"
    AS = "Asia"
    AF = "Africa"
    OC = "Oceania"
    ME = "Middle East"
    GLOBAL = "Global"

# --- Base Intelligence Object ---

class IntelligenceObject(BaseModel):
    """Base class for all tracked intelligence entities."""
    id: str = Field(..., description="Unique identifier for the object")
    source_urls: List[HttpUrl] = Field(default_factory=list, description="List of source URLs for this data")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.CLAIMED, description="Confidence level of this intelligence")
    last_updated: date = Field(default_factory=date.today, description="Date this record was last updated")
    notes: Optional[str] = Field(None, description="Analyst notes or context")

# --- Core Domain Models ---

class Organization(IntelligenceObject):
    """Represents a company, government body, or consortium."""
    name: str
    country_of_origin: str
    aliases: List[str] = []
    parent_org_id: Optional[str] = None
    sector: Optional[str] = None # e.g., "Hyperscale", "Telecom", "Government"

class GeoLocation(BaseModel):
    """Standardized geospatial location."""
    latitude: float
    longitude: float
    country: str
    city: Optional[str] = None
    region: Region = Region.GLOBAL

class DataCenter(IntelligenceObject):
    """Physical facility housing compute infrastructure."""
    type: Literal["datacenter"] = "datacenter"
    name: str = Field(..., description="Facility name (e.g., 'LHR14')")
    owner_id: str = Field(..., description="ID of the owner organization")
    operator_id: Optional[str] = Field(None, description="ID of the operator if different from owner")
    location: GeoLocation
    status: EntityStatus
    capacity_mw: Optional[float] = Field(None, description="Power capacity in Megawatts")
    gross_floor_area_sqft: Optional[int] = None
    rfs_date: Optional[date] = Field(None, description="Ready For Service date")
    properties: dict = Field(default_factory=dict, description="Flexible property bag for extra metadata")

class SubseaCable(IntelligenceObject):
    """Submarine fiber optic cable system."""
    type: Literal["cable"] = "cable"
    name: str
    owners: List[str] = Field(default_factory=list, description="List of owner IDs")
    suppliers: List[str] = Field(default_factory=list, description="List of supplier IDs (e.g., SubCom, ASN)")
    length_km: Optional[float] = None
    landing_points: List[GeoLocation] = Field(default_factory=list, description="List of landing station locations")
    status: EntityStatus
    rfs_date: Optional[date] = None
    fiber_pairs: Optional[int] = None
    design_capacity_tbps: Optional[float] = None
    geometry_coordinates: Optional[List[List[List[float]]]] = Field(None, description="MultiLineString coordinates [[lat,lon],...]")
