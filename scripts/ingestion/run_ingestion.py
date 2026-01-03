import typer
import logging
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from typing import Optional

# Adjust import path if running as script vs module
import sys
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))

from atlas_gridwatch.ingestion import FileIngestor, SeedDataIngestor, TeleGeographyIngestor
# New modules
from atlas_gridwatch.ingestion_rss import RSSIngestor
from atlas_gridwatch.llm_analysis import LLMAnalyzer
from atlas_gridwatch.models import DataCenter, EntityStatus, GeoLocation
from atlas_gridwatch.normalization import NormalizationEngine
from atlas_gridwatch.database import InfrastructureDatabase
from atlas_gridwatch.ingestion_epoch import EpochIngestor

app = typer.Typer()
console = Console()

@app.command()
def main(
    source: str = typer.Option(..., help="Source: 'telegeography', 'seed', 'rss', or file path"),
    output: Path = typer.Option(Path("data/processed/infrastructure_master.json"), help="Output path (Master DB)")
):
    """
    Ingests data, normalizes it, and persists to the Master Database.
    """
    console.rule("[bold blue]Atlas Gridwatch Ingestion Pipeline[/bold blue]")
    
    # Initialize DB
    db = InfrastructureDatabase(output)
    console.log(f"Opened Database at {output} with {len(db.data)} records.")
    
    raw_data = [] # List of Dicts
    assets_to_save = [] # List of DataCenter objects

    # --- SOURCE HANDLERS ---
    
    if source == "seed":
        console.log("[green]Ingesting from internal Seed Data...[/green]")
        ingestor = SeedDataIngestor()
        raw_data = ingestor.fetch()
        console.log(f"Fetched {len(raw_data)} raw items.")
        
        # 2. Normalization
        console.log("[yellow]Normalizing data...[/yellow]")
        engine = NormalizationEngine()
        normalized_data = engine.normalize(raw_data)
        console.log(f"Normalized {len(normalized_data)} items successfully.")

    elif source == "telegeography":
        console.log("[blue]Ingesting from TeleGeography Public API...[/blue]")
        ingestor = TeleGeographyIngestor()
        raw_data = ingestor.fetch()
        console.log(f"Fetched {len(raw_data)} raw items.")

        # 2. Normalization
        console.log("[yellow]Normalizing data...[/yellow]")
        engine = NormalizationEngine()
        normalized_data = engine.normalize(raw_data)
        console.log(f"Normalized {len(normalized_data)} items successfully.")

    elif source == "rss":
        console.log("[cyan]Ingesting from OSINT RSS Feeds...[/cyan]")
        rss = RSSIngestor()
        items = rss.fetch()
        console.log(f"Found {len(items)} news items. Engaging AI Analyst for extraction...")
        
        llm = LLMAnalyzer()
        
        extracted_assets = []
        for item in items:
            # AI Extraction
            console.print(f"Analyzing: [italic]{item['title']}[/italic]")
            try:
                data = llm.extract_entity_from_text(f"{item['title']}\n{item['summary']}")
            except Exception as e:
                console.print(f"   [red]AI Error[/red]: {e}")
                continue

            if data and data.get("found", True) and data.get("name"):
                 pass # Logic continues below
            else:
                 console.print(f"   [dim]Skipped: {data}[/dim]")
                 continue

            if data and data.get("name"):
                # Convert to DataCenter object
                # We need a Geocoder ideally, for now we let Normalizer handle it or use placeholders
                # Normalizer has _normalize_location but it relies on string parsing.
                # Let's trust the AI extracted City/Country
                
                # Manual Object Construction for now
                try:
                    dc = DataCenter(
                        id=f"rss_{hash(item['link'])}",
                        name=data.get("name"),
                        owner_id=data.get("owner", "Unknown"),
                        location=GeoLocation(
                            city=data.get("city"), 
                            country=data.get("country"),
                        location=GeoLocation(
                            city=data.get("city"), 
                            country=data.get("country"),
                            region="Global", # Fix: Must be valid Enum
                            latitude=data.get("latitude", 0.0),
                            longitude=data.get("longitude", 0.0)
                        ),
                            latitude=data.get("latitude", 0.0),
                            longitude=data.get("longitude", 0.0)
                        ),
                        status=EntityStatus.PLANNED if "plan" in data.get("status", "").lower() else EntityStatus.ACTIVE,
                        properties={"intent": data.get("intent"), "source_url": item['link']}
                    )
                    extracted_assets.append(dc)
                    console.print(f"   [green]EXTRACTED[/green]: {dc.name} ({dc.status.value})")
                except Exception as e:
                    console.print(f"   [red]Validation Error[/red]: {e}")
        
        # We need a way to MERGE this with existing master list if we want map to show both.
        # For now, let's just save these as the 'infrastructure_master' or Append?
        # The script overwrites by default. 
        # Strategy: Read existing, append new, save.
        
        if output.exists():
            with open(output, 'r') as f:
                existing = json.load(f)
            console.log(f"Merging with {len(existing)} existing records...")
            # Simple conversion of existing dicts back to list? 
            # Actually, we can just append dict representation of new assets
            final_data = existing + [asset.model_dump(mode='json') for asset in extracted_assets]
        else:
            final_data = [asset.model_dump(mode='json') for asset in extracted_assets]
            
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, "w") as f:
            json.dump(final_data, f, indent=2)
            
        console.log(f"[bold green]Success![/bold green] Added {len(extracted_assets)} AI-extracted assets.")
        return # Exit early as we handled persistence manually

    elif Path(source).exists():
        console.log(f"[green]Ingesting from file: {source}...[/green]")
        ingestor = FileIngestor(source)
        raw_data = ingestor.fetch()
        console.log(f"Fetched {len(raw_data)} raw items.")

        # 2. Normalization
        console.log("[yellow]Normalizing data...[/yellow]")
        engine = NormalizationEngine()
        normalized_data = engine.normalize(raw_data)
        console.log(f"Normalized {len(normalized_data)} items successfully.")

    elif source == "seed_file":
        # Manual Seed Loading (e.g. Frontier AI)
        seed_path = Path("data/seeds/frontier_ai_seed.json")
        if seed_path.exists():
            console.log(f"[green]Loading Seed File: {seed_path}...[/green]")
            with open(seed_path, 'r') as f:
                raw_seeds = json.load(f)
                # Convert raw dicts to DataCenter objects
                for s in raw_seeds:
                    try:
                        dc = DataCenter(**s)
                        assets_to_save.append(dc)
                    except Exception as e:
                        console.print(f"[red]Seed Error[/red]: {e} in {s['name']}")
    elif source == "epoch":
        console.log("[magenta]Ingesting from Epoch AI Dataset...[/magenta]")
        file_path = Path("data/raw/data_centers_epochAI/data_centers.csv")
        
        if not file_path.exists():
             console.log(f"[red]Epoch file not found at {file_path}[/red]")
        else:
            ingestor = EpochIngestor(file_path)
            raw_data = ingestor.fetch()
            console.log(f"Fetched {len(raw_data)} raw items from Epoch AI.")
    
    # --- NORMALIZATION & CONVERSION ---
    if raw_data:
        console.log("[yellow]Normalizing raw data...[/yellow]")
        engine = NormalizationEngine()
        normalized_models = engine.normalize(raw_data)
        console.log(f"Normalized {len(normalized_models)} items.")
        assets_to_save.extend(normalized_models)

    # --- PERSISTENCE ---
    if assets_to_save:
        console.log(f"Upserting {len(assets_to_save)} assets to Database...")
        db.bulk_upsert(assets_to_save)
        console.log(f"[bold green]Sync Complete.[/bold green] DB now contains {len(db.data)} records.")
    else:
        console.log("[yellow]No new assets to ingest.[/yellow]")

    # Preview from DB
    table = Table(title="Database Preview (Top 5)")
    table.add_column("Name", style="magenta")
    table.add_column("Owner", style="cyan")
    table.add_column("Status", style="green")
    
    # Show first 5 from DB
    preview_items = list(db.data.values())[:5]
    for item in preview_items:
        table.add_row(
            item.get("name", "Unknown"),
            str(item.get("owner_id", "Unknown")),
            item.get("status", "Unknown")
        )
    console.print(table)

if __name__ == "__main__":
    app()
