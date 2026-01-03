import csv
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

class BriefGenerator:
    """
    Generates HTML intelligence briefs from analysis outputs.
    """

    def __init__(self, template_dir: Path):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template("brief_template.html")

    def load_csv(self, path: Path) -> List[Dict[str, Any]]:
        """Reads a CSV file into a list of dicts."""
        if not path.exists():
            return []
        with open(path, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def generate(self, 
                 nodes_path: Path, 
                 risk_path: Path,
                 strategic_assessment: str,
                 output_path: Path):
        """
        Renders the brief.
        """
        
        # Load Data
        critical_nodes = self.load_csv(nodes_path)
        
        # Parse Risk CSV properly
        jurisdiction_stats = {}
        risk_data = self.load_csv(risk_path)
        for row in risk_data:
            jurisdiction_stats[row['Jurisdiction']] = row['Asset_Count']

        # Type conversion for template formatting
        for node in critical_nodes:
            try:
                node['betweenness'] = float(node['betweenness'])
            except:
                node['betweenness'] = 0.0

        # Render
        html = self.template.render(
            generation_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            critical_nodes=critical_nodes,
            jurisdiction_stats=jurisdiction_stats,
            strategic_assessment=strategic_assessment
        )

        # Write
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
