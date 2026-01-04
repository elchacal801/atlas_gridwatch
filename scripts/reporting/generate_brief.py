import typer
import sys
from pathlib import Path
from rich.console import Console

# Adjust import path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))

from atlas_gridwatch.reporting import BriefGenerator

app = typer.Typer()
console = Console()

@app.command()
def create(
    nodes_path: Path = typer.Option(Path("data/outputs/critical_nodes.csv"), help="Input critical nodes CSV"),
    risk_path: Path = typer.Option(Path("data/outputs/jurisdiction_risk.csv"), help="Input risk CSV"),
    ai_path: Path = typer.Option(Path("data/outputs/ai_assessment.html"), help="Input AI assessment HTML file"),
    output_path: Path = typer.Option(Path("data/outputs/intelligence_brief.html"), help="Output HTML file")
):
    """
    Generate an HTML Intelligence Brief.
    """
    console.rule("[bold magenta]Atlas Gridwatch Reporting[/bold magenta]")
    
    # Locate templates relative to the package
    template_dir = Path(__file__).resolve().parents[2] / 'src' / 'atlas_gridwatch' / 'templates'
    
    if not template_dir.exists():
        console.print(f"[bold red]Error[/bold red]: Template directory {template_dir} not found.")
        raise typer.Exit(1)

    console.log(f"Using template from: {template_dir}")
    
    generator = BriefGenerator(template_dir)
    
    try:
        # Read the AI assessment content
        strategic_assessment_content = ai_path.read_text(encoding="utf-8")
        
        # Read News Analysis if available
        import json
        news_file = Path("data/outputs/news_analysis.json")
        news_data = []
        if news_file.exists():
            with open(news_file, 'r', encoding='utf-8') as f:
                news_data = json.load(f)
            console.log(f"Loaded {len(news_data)} news items.")

        # Read Growth Metrics if available
        growth_file = Path("data/outputs/growth_metrics.json")
        growth_data = None
        if growth_file.exists():
            with open(growth_file, 'r', encoding='utf-8') as f:
                growth_data = json.load(f)
            console.log(f"Loaded Growth Metrics.")

        generator.generate(nodes_path, risk_path, strategic_assessment_content, output_path, news_analysis=news_data, growth_metrics=growth_data)
        console.log(f"[bold green]Success![/bold green] Brief saved to {output_path}")
        console.print(f"Open '{output_path}' in your browser to view.")
    except Exception as e:
        console.print(f"[bold red]Failed to generate brief:[/bold red] {e}")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
