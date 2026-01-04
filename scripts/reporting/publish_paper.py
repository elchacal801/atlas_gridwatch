import typer
import markdown
import jinja2
from pathlib import Path
from rich.console import Console

app = typer.Typer()
console = Console()

# Setup Jinja2 Environment
TEMPLATE_DIR = Path("src/atlas_gridwatch/templates")
env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

@app.command()
def publish(
    input_path: Path = typer.Argument(..., help="Path to the markdown paper"),
    output_dir: Path = typer.Option(Path("docs/research"), help="Directory to save HTML output")
):
    """
    Converts a Markdown research paper into a distinct HTML page with data handling.
    """
    if not input_path.exists():
        console.print(f"[red]Error: File {input_path} not found.[/red]")
        raise typer.Exit(code=1)

    console.rule(f"[bold blue]Publishing: {input_path.name}[/bold blue]")

    # 1. Read Markdown
    with open(input_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # 2. Extract Metadata (YAML Frontmatter style if needed, or simple parsing)
    # For now, we assume the first line is the Title (# Title)
    lines = md_content.split('\n')
    title = "Atlas Gridwatch Research"
    if lines and lines[0].startswith("# "):
        title = lines[0].replace("# ", "").strip()
        # Remove title from body to avoid duplicate h1
        md_content = "\n".join(lines[1:])

    # 3. Convert to HTML
    html_body = markdown.markdown(md_content, extensions=['extra', 'tables', 'fenced_code'])

    # 4. Data Injection (Placeholder)
    # This is where we would replace [[EMBED:MAP]] with actual iframe/divs
    # For now, we'll just handle basic strings if present
    html_body = html_body.replace("[[EMBED:GLOBAL_MAP]]", 
        '<iframe src="../atlas_gridwatch_map.html" style="width:100%; height:500px; border:1px solid #333;"></iframe>')

    # 5. Render Template
    template = env.get_template("research_paper.html")
    final_html = template.render(
        title=title,
        content=html_body,
        generation_date="2026-01-04" # Dynamic later
    )

    # 6. Save
    output_dir.mkdir(parents=True, exist_ok=True)
    slug = input_path.stem
    output_file = output_dir / f"{slug}.html"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    console.print(f"[green]Successfully published to {output_file}[/green]")

if __name__ == "__main__":
    app()
