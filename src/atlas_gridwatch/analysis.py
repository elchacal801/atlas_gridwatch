import networkx as nx
from typing import List, Dict, Any, Tuple
from .models import DataCenter, SubseaCable, GeoLocation, EntityStatus
import logging

logger = logging.getLogger(__name__)

class GeopoliticalEnricher:
    """
    Enriches entities with geopolitical context (Jurisdiction, Sovereign alignment).
    """
    
    # MVP Hardcoded lookup. In future, this comes from a database.
    # Maps Owner/Operator Name -> Origin Country
    KNOWN_ENTITIES = {
        "equinix": "USA",
        "digital realty": "USA",
        "aws": "USA",
        "amazon": "USA",
        "microsoft": "USA",
        "google": "USA",
        "meta": "USA",
        "facebook": "USA",
        "huawei": "China",
        "alibaba": "China",
        "tencent": "China",
        "china mobile": "China",
        "china telecom": "China",
        "china unicom": "China",
        "orange": "France",
        "telehouse": "Japan", # KDDI
        "kddi": "Japan",
        "ntt": "Japan",
        "telxius": "Spain",
        "vodafone": "UK",
    }

    def get_jurisdiction(self, entity_name: str) -> str:
        """Derives the effective jurisdiction of an entity based on its name."""
        name_lower = entity_name.lower()
        for key, country in self.KNOWN_ENTITIES.items():
            if key in name_lower:
                return country
        return "Unknown"

class NetworkAnalyzer:
    """
    Builds a graph of the global infrastructure to identify strategic nodes.
    """
    
    def __init__(self, items: List[Any]):
        self.graph = nx.Graph()
        self._build_graph(items)
        
    def _build_graph(self, items: List[Any]):
        """Constructs the network graph from DataCenters and Cables."""
        
        # 1. Add DataCenters as Nodes
        for item in items:
            if isinstance(item, DataCenter):
                # Node attributes
                self.graph.add_node(
                    item.id, 
                    type="datacenter", 
                    name=item.name,
                    country=item.location.country,
                    owner=item.owner_id
                )
        
        # 2. Add Cables as Edges (or sets of edges)
        # For MVP, we assume cables connect Regions or landing points.
        # This is tricky without exact colocation data. 
        # Strategy: Connect all landing points of a cable to each other (mesh).
        
        # First, we need to map Landing Points to nearest DataCenters or create 'LandingStation' nodes.
        # For this MVP, we will treat Landing Points as abstract nodes if they don't match a DC.
        
        for item in items:
            if isinstance(item, SubseaCable):
                if not item.landing_points:
                    continue
                    
                # Create nodes for landing points if they act as connectors
                lp_ids = []
                for i, lp in enumerate(item.landing_points):
                    # In a real system, we'd spatial join to valid DCs.
                    # Here, we create a temporary landing point ID
                    lp_id = f"lp_{item.name}_{lp.country}_{i}"
                    if not self.graph.has_node(lp_id):
                        self.graph.add_node(
                            lp_id,
                            type="landing_point",
                            name=f"{item.name} Landing - {lp.country}",
                            country=lp.country
                        )
                    lp_ids.append(lp_id)
                
                # Connect all LPs in this cable (clique)
                # A cable connects all its points.
                import itertools
                for u, v in itertools.combinations(lp_ids, 2):
                    self.graph.add_edge(
                        u, v, 
                        cable_name=item.name,
                        owners=item.owners
                    )

    def calculate_criticality(self) -> List[Dict[str, Any]]:
        """
        Calculates Betweenness Centrality to find chokepoints.
        Returns sorted list of critical nodes.
        """
        if self.graph.number_of_nodes() == 0:
            return []
            
        centrality = nx.betweenness_centrality(self.graph)
        degree = nx.degree_centrality(self.graph)
        
        results = []
        for node_id, score in centrality.items():
            node_data = self.graph.nodes[node_id]
            results.append({
                "id": node_id,
                "name": node_data.get("name"),
                "type": node_data.get("type"),
                "country": node_data.get("country"),
                "betweenness": score,
                "degree": degree.get(node_id, 0)
            })
            
        # Sort by Betweenness (descending)
        return sorted(results, key=lambda x: x["betweenness"], reverse=True)
