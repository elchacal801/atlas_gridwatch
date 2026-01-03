import typer
import json
import csv
from pathlib import Path
from rich.console import Console
from rich.table import Table
import sys

# Adjust import path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))

from atlas_gridwatch.models import DataCenter, SubseaCable, EntityStatus
from atlas_gridwatch.analysis import NetworkAnalyzer, GeopoliticalEnricher
from atlas_gridwatch.llm_analysis import LLMAnalyzer

app = typer.Typer()
console = Console()

@app.command()
def analyze(
    input_path: Path = typer.Option(Path("data/processed/infrastructure_master.json"), help="Input processed data"),
    output_dir: Path = typer.Option(Path("data/outputs"), help="Directory for analysis outputs")
):
    """
    Run strategic analysis: Criticality (Chokepoints) and Geopolitical Risk.
    """
    console.rule("[bold red]Atlas Gridwatch Strategic Analysis[/bold red]")

    # 1. Load Data
    if not input_path.exists():
        console.print(f"[bold red]Error[/bold red]: {input_path} not found.")
        raise typer.Exit(1)

    with open(input_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    
    # deserialize back to objects
    items = []
    for item in raw_data:
        t = item.get("type")
        try:
            if t == "datacenter":
                items.append(DataCenter(**item))
            elif t == "cable":
                items.append(SubseaCable(**item))
        except Exception as e:
            console.log(f"[red]Failed to load item {item.get('name')}: {e}[/red]")
    
    console.log(f"Loaded {len(items)} assets for analysis.")

    # 2. Geopolitical Enrichment
    console.log("[yellow]Enriching with Geopolitical Data...[/yellow]")
    enricher = GeopoliticalEnricher()
    
    jurisdiction_counts = {}
    
    for item in items:
        # Check owners
        owners = []
        if isinstance(item, DataCenter):
            owners = [item.owner_id]
        elif isinstance(item, SubseaCable):
            owners = item.owners
            
        for owner in owners:
            jurisdiction = enricher.get_jurisdiction(owner)
            jurisdiction_counts[jurisdiction] = jurisdiction_counts.get(jurisdiction, 0) + 1
            
    # Output Risk Report
    output_dir.mkdir(parents=True, exist_ok=True)
    risk_file = output_dir / "jurisdiction_risk.csv"
    with open(risk_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Jurisdiction", "Asset_Count"])
        for country, count in jurisdiction_counts.items():
            writer.writerow([country, count])
            
    console.log(f"Saved Jurisdiction Report to {risk_file}")

    # 3. Network Analysis
    console.log("[yellow]Running Network Graph Analysis...[/yellow]")
    analyzer = NetworkAnalyzer(items)
    critical_nodes = analyzer.calculate_criticality()
    
    critical_file = output_dir / "critical_nodes.csv"
    with open(critical_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["id", "name", "type", "country", "betweenness", "degree"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for node in critical_nodes:
            writer.writerow(node)
            
    console.log(f"Saved Critical Nodes to {critical_file}")
    
    # 4. Preview
    table = Table(title="Top Strategic Chokepoints")
    table.add_column("Name", style="cyan")
    table.add_column("Country", style="green")
    table.add_column("Betweenness Score", style="magenta")
    
    for node in critical_nodes[:5]:
        b_score = f"{node['betweenness']:.4f}"
        table.add_row(node['name'], node['country'], b_score)
        
    console.print(table)

    # 5. AI Strategic Assessment
    console.rule("[bold purple]AI Strategic Assessment[/bold purple]")
    console.log("Engaging LLM Analyst for PIR assessment...")
    
    # Filter for Planned/Frontier AI
    planned_assets = [item for item in items if isinstance(item, DataCenter) and item.status == EntityStatus.PLANNED]
    
    llm = LLMAnalyzer()
    assessment_context = {
        "critical_nodes": critical_nodes,
        "jurisdiction_risk": jurisdiction_counts,
        "planned_assets": [a.model_dump() for a in planned_assets] # Pass full details
    }
    
    assessment_text = llm.generate_assessment(assessment_context)
    
    # Save assessment
    ai_file = output_dir / "ai_assessment.html"
    with open(ai_file, 'w', encoding='utf-8') as f:
        f.write(assessment_text)
        
    console.log(f"Saved Strategic Assessment to {ai_file}")
    console.print("[italic]Assessment Preview:[/italic]")
    console.print(assessment_text[:200] + "...")

    # 6. Strategic News Analysis
    console.rule("[bold cyan]Strategic News Analysis[/bold cyan]")
    news_file = Path("data/processed/news_stream.json")
    if news_file.exists():
        console.log("Loading raw news stream...")
        with open(news_file, 'r', encoding='utf-8') as f:
            raw_news = json.load(f)
        
        console.log("Analyzing news for intelligence value...")
        news_intelligence = llm.analyze_news_items(raw_news)
        
        news_output = output_dir / "news_analysis.json"
        with open(news_output, 'w', encoding='utf-8') as f:
            json.dump(news_intelligence, f, indent=2)
            
        console.log(f"Saved {len(news_intelligence)} intelligence events to {news_output}")
    else:
        console.log("[dim]No news stream found. Skipping news analysis.[/dim]")


if __name__ == "__main__":
    app()
