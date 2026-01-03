import typer
import json
import sys
from pathlib import Path
from rich.console import Console

# Adjust import path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))

from atlas_gridwatch.models import DataCenter, SubseaCable
from atlas_gridwatch.visualization import MapVisualizer

app = typer.Typer()
console = Console()

@app.command()
def plot(
    input_path: Path = typer.Option(Path("data/processed/infrastructure_master.json"), help="Input processed data"),
    output_path: Path = typer.Option(Path("data/outputs/atlas_gridwatch_map.html"), help="Output HTML file")
):
    """
    Generate an interactive intelligence map.
    """
    console.rule("[bold green]Atlas Gridwatch Visualization[/bold green]")
    
    if not input_path.exists():
        console.print(f"[bold red]Error[/bold red]: {input_path} not found.")
        raise typer.Exit(1)

    with open(input_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    # Deserialize (Simple method)
    items = []
    for item in raw_data:
        t = item.get("type")
        try:
            if t == "datacenter":
                items.append(DataCenter(**item))
            elif t == "cable":
                items.append(SubseaCable(**item))
        except Exception as e:
            console.log(f"[red]Skipping {item.get('name')}: {e}[/red]")

    console.log(f"Loaded {len(items)} items for plotting.")

    # Visualize
    viz = MapVisualizer()
    
    for item in items:
        if isinstance(item, DataCenter):
            viz.add_datacenter(item)
        elif isinstance(item, SubseaCable):
            viz.add_cable(item)
            
    # Save
    output_path.parent.mkdir(parents=True, exist_ok=True)
    viz.save(str(output_path))
    
    console.log(f"[bold green]Success![/bold green] Map saved to {output_path}")
    console.print(f"Open '{output_path}' in your browser to view.")

if __name__ == "__main__":
    app()
