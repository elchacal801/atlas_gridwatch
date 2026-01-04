import folium
from folium import plugins
from jinja2 import Template
from typing import List, Union
from .models import DataCenter, SubseaCable, EntityStatus

class MapVisualizer:
    """
    Generates interactive Leaflet maps from Intelligence Objects.
    """

    def __init__(self, center_lat: float = 20.0, center_lon: float = 0.0, zoom: int = 2):
        self.m = folium.Map(
            location=[center_lat, center_lon], 
            zoom_start=3, 
            tiles=None, 
            prefer_canvas=True,
            world_copy_jump=True,
            min_zoom=2
        )
        
        # Base Layer
        folium.TileLayer(
            "CartoDB dark_matter",
            name="Dark Matter",
            bounds=[[-90, -180], [90, 180]]
        ).add_to(self.m)
        
        # Custom CSS for Background and Labels
        # Widescreen 16:9 fixed container
        self.m.get_root().html.add_child(folium.Element("""
            <style>
                body {
                    background-color: #1a1a1a;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                #map {
                    width: 90vw !important;
                    height: 50.625vw !important; /* 16:9 Aspect Ratio based on width */
                    max-height: 90vh;
                    max-width: 160vh; /* Maintain ratio if height constrained */
                    box-shadow: 0 0 20px rgba(0,0,0,0.8);
                    border: 1px solid #333;
                }
                .leaflet-container { background: #000000 !important; }
                .map-label { 
                    font-size: 9px; 
                    color: rgba(255,255,255,0.6); 
                    font-family: 'Segoe UI', sans-serif; 
                    text-shadow: 1px 1px 2px #000;
                    white-space: nowrap;
                    pointer-events: none;
                    opacity: 0.8;
                }
                .label-major {
                    font-size: 11px;
                    font-weight: bold;
                    color: rgba(255,255,255,0.9);
                }
                .legend-box {
                    position: fixed; 
                    bottom: 20px; 
                    right: 20px; 
                    width: 160px;
                    z-index: 1000; 
                    font-size: 11px;
                    background-color: rgba(10, 15, 30, 0.85); /* Darker blue-black */
                    padding: 12px;
                    border: 1px solid #34495e;
                    color: #ecf0f1;
                    border-radius: 6px;
                    font-family: 'Segoe UI', sans-serif;
                    backdrop-filter: blur(4px);
                }
                .legend-title { font-weight: 700; margin-bottom: 8px; font-size: 12px; color: #3498db; }
                .legend-item { display: flex; align-items: center; margin-bottom: 5px; }
                .legend-color { width: 10px; height: 10px; margin-right: 10px; border-radius: 50%; }
            </style>
        """))
        
        # Legend
        legend_html = """
        <div class="legend-box">
            <div class="legend-title">INFRASTRUCTURE KEY</div>
            <div class="legend-item"><div class="legend-color" style="background:#DB4437; box-shadow: 0 0 5px #DB4437;"></div>Google</div>
            <div class="legend-item"><div class="legend-color" style="background:#4267B2; box-shadow: 0 0 5px #4267B2;"></div>Meta</div>
            <div class="legend-item"><div class="legend-color" style="background:#FF9900; box-shadow: 0 0 5px #FF9900;"></div>Amazon</div>
            <div class="legend-item"><div class="legend-color" style="background:#7FBA00; box-shadow: 0 0 5px #7FBA00;"></div>Microsoft</div>
            <div class="legend-item"><div class="legend-color" style="background:#00FFFF; box-shadow: 0 0 5px #00FFFF;"></div>Telecom/Consortium</div>
            <div class="legend-item"><div class="legend-color" style="background:#2ecc71; box-shadow: 0 0 5px #2ecc71;"></div>Active Data Center</div>
            <div class="legend-item"><div class="legend-color" style="background:#9b59b6; box-shadow: 0 0 5px #9b59b6; border: 1px dashed white;"></div>Planned / Frontier AI</div>
        </div>
        """
        self.m.get_root().html.add_child(folium.Element(legend_html))
        
        # Create Feature Groups
        self.cable_layer = folium.FeatureGroup(name="Subsea Cables (Physical)")
        self.dc_layer = folium.FeatureGroup(name="Data Centers")
        self.label_layer = folium.FeatureGroup(name="Labels", show=True)
        self.heat_layer_group = folium.FeatureGroup(name="Infrastructure Density", show=False)
        self.heat_data = []

        self.m.add_child(self.cable_layer)
        self.m.add_child(self.dc_layer)
        self.m.add_child(self.label_layer)
        self.m.add_child(self.heat_layer_group)
        
    def _get_owner_color(self, owners: List[str]) -> str:
        """Determines color based on ownership."""
        owners_str = " ".join(owners).lower()
        if "google" in owners_str: return "#DB4437" # Red
        if "meta" in owners_str or "facebook" in owners_str: return "#4267B2" # Blue
        if "microsoft" in owners_str: return "#7FBA00" # Green
        if "amazon" in owners_str or "aws" in owners_str: return "#FF9900" # Orange
        return "#00FFFF" # Cyan (Default)

    def add_datacenter(self, dc: DataCenter):
        """Adds a Data Center marker."""
        if dc.status == EntityStatus.ACTIVE:
            color = "#2ecc71" # Emerald Green
            fill_opacity = 0.8
        elif dc.status == EntityStatus.PLANNED:
            color = "#9b59b6" # Amethyst Purple
            fill_opacity = 0.5
        else:
             color = "#f1c40f" # Sunflower (Inactive/Other)
             fill_opacity = 0.8
        
        popup_html = f"""
        <div style="font-family: sans-serif; min-width: 200px;">
            <h4 style="margin: 0; color: {color};">{dc.name}</h4>
            <hr style="border: 0; border-top: 1px solid #555; margin: 5px 0;">
            <b>Owner:</b> {dc.owner_id}<br>
            <b>Status:</b> {dc.status.value.upper()}<br>
            <b>Loc:</b> {dc.location.city}, {dc.location.country}<br>
            <em style="font-size: 0.9em; color: #aaa;">{dc.properties.get('intent', '')}</em>
            {f'<hr><a href="{dc.properties.get("source_url")}" target="_blank" style="color:#3498db">Source</a>' if dc.properties.get('source_url') else ''}
        </div>
        """
        
        folium.CircleMarker(
            location=[dc.location.latitude, dc.location.longitude],
            radius=6 if dc.status == EntityStatus.ACTIVE else 8,
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=f"{dc.name} ({dc.status.value.upper()})",
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=fill_opacity,
            weight=1,
            dash_array='5,5' if dc.status == EntityStatus.PLANNED else None
        ).add_to(self.dc_layer)
        
        # Add Label for DC
        folium.Marker(
            location=[dc.location.latitude + 0.5, dc.location.longitude], # Slight offset
            icon=folium.DivIcon(html=f'<div class="map-label">{dc.location.city or dc.name}</div>')
        ).add_to(self.label_layer)
        
        # Add to heatmap
        self.heat_data.append([dc.location.latitude, dc.location.longitude, 1.0])

    def add_cable(self, cable: SubseaCable):
        """Adds a Subsea Cable polyline with AntPath animation."""
        
        # Geometry Logic
        paths = []
        if cable.geometry_coordinates:
            # Already formatted as list of segments [[lat,lon],...]
            paths = cable.geometry_coordinates
        elif cable.landing_points and len(cable.landing_points) >= 2:
            # Fallback to straight lines, but handle Dateline crossing (Pacific)
            # If dLong > 180, we must wrap one coordinate.
            
            raw_path = []
            for i, lp in enumerate(cable.landing_points):
                lat, lon = lp.latitude, lp.longitude
                
                if i > 0:
                    prev_lat, prev_lon = raw_path[-1]
                    delta = lon - prev_lon
                    
                    # Check for dateline crossing
                    if delta > 180:
                        lon -= 360
                    elif delta < -180:
                        lon += 360
                
                raw_path.append((lat, lon))
            
            paths = [raw_path]
        else:
            return

        color = self._get_owner_color(cable.owners)

        popup_html = f"""
         <div style="font-family: sans-serif;">
            <h5 style="margin: 0; color: {color};">{cable.name}</h5>
            <b>Owners:</b> {', '.join(cable.owners[:3])}{'...' if len(cable.owners)>3 else ''}<br>
            <b>Status:</b> {cable.status.value}<br>
        </div>
        """
        
        # Render each segment
        for path in paths:
             plugins.AntPath(
                locations=path,
                popup=folium.Popup(popup_html, max_width=300),
                tooltip=cable.name,
                color=color,
                pulse_color="#ffffff", # White pulse
                delay=1000,
                weight=2,
                opacity=0.8
            ).add_to(self.cable_layer)
             
        # Add Label at the 'middle' of the cable logic is hard with MultiLineString
        # Simplified: Use the first point of the first segment for now, or just don't label every cable?
        # Let's label only major ones (or all for now).
        # Better: Midpoint of longest segment.
        try:
            # Find longest segment
            longest = max(paths, key=len)
            if len(longest) > 2:
                mid = longest[len(longest)//2]
                folium.Marker(
                    location=mid,
                    icon=folium.DivIcon(html=f'<div class="map-label" style="color:{color}">{cable.name}</div>')
                ).add_to(self.label_layer)
        except:
            pass
            

    def save(self, path: str):
        """Saves the map to an HTML file."""
        # Add Heatmap if we have data
        if self.heat_data:
            plugins.HeatMap(
                self.heat_data, 
                name="Density Heatmap",
                min_opacity=0.3, radius=15, blur=10,
                gradient={0.4: 'blue', 0.65: 'lime', 1: 'red'}
            ).add_to(self.heat_layer_group)
        
        folium.LayerControl(collapsed=False).add_to(self.m)
        self.m.save(path)
