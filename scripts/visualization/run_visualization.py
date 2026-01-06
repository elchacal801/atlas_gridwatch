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

    
    # --- Generate Subsea Map ---
    console.rule("[blue]Generating Subsea Map[/blue]")
    viz_subsea = MapVisualizer(mode='subsea')
    for item in items:
        if isinstance(item, SubseaCable):
            viz_subsea.add_cable(item)
        # No DCs in subsea mode
            
    out_subsea = output_path.parent / "map_subsea.html"
    out_subsea.parent.mkdir(parents=True, exist_ok=True)
    viz_subsea.save(str(out_subsea))
    console.log(f"[bold green]Success![/bold green] Subsea Map saved to {out_subsea}")

    # --- Generate Cloud Map ---
    console.rule("[cyan]Generating Cloud Map[/cyan]")
    viz_cloud = MapVisualizer(mode='cloud')
    for item in items:
        if isinstance(item, DataCenter):
            viz_cloud.add_datacenter(item)
        elif isinstance(item, SubseaCable):
            viz_cloud.add_cable(item)
            
    out_cloud = output_path.parent / "map_cloud.html"
    viz_cloud.save(str(out_cloud))
    console.log(f"[bold green]Success![/bold green] Cloud Map saved to {out_cloud}")
    
    # Keep legacy output for backward compatibility if needed, or just warn
    console.print(f"Generated 'map_subsea.html' and 'map_cloud.html'.")

if __name__ == "__main__":
    app()
