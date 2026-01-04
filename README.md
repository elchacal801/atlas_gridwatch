# Atlas Gridwatch
**Strategic Intelligence on Global Compute & Connectivity Infrastructure**

> **STATUS**: Pre-Alpha / Active Development
> **MISSION**: To map, analyze, and visualize the global physical backbone of AI, cloud compute, and digital power for strategic intelligence purposes.
> **ACCESS**: [**Live Intelligence Portal**](https://elchacal801.github.io/atlas_gridwatch/)

## Mission & Purpose
Atlas Gridwatch is a continuously maintained, intelligence-grade platform. It goes beyond static mapping to generate **strategic intelligence** regarding:
- **Geopolitical Intent**: How nations project power through digital infrastructure.
- **Corporate Strategy**: The physical footprint of hyperscalers and sovereign clouds.
- **Systemic Risk**: Concentration, chokepoints, and resilience of the global grid.

## Core Capabilities
1. **Multi-Source Ingestion**: Aggregating data from regulatory filings, industry datasets, and satellite-derived analysis.
2. **Unified Intelligence Schema**: Normalizing disparate data into a coherent model of *Locations*, *Assets*, and *Ownership*.
3. **Strategic Visualization**: High-signal visual analytics designed for intelligence briefings and decision support.
4. **AI Strategic Analyst**: Automated assessment using **Gemini 2.0 Flash** and **RAG** (Retrieval Augmented Generation) to synthesize local research papers and real-time news into classified-style briefs.

## Strategic Objectives
Atlas Gridwatch is designed to answer specific Priority Intelligence Requirements (PIRs):

### 1. Maritime Resilience & Chokepoints (Systemic Risk)
- **Objective**: Monitor the physical vulnerability of the global subsea cable network.
- **Focus**: Identify single points of failure (Straits of Malacca, Suez, Luzon) where kinetic or hybrid disruption could sever global connectivity.
- **Metric**: Betweenness centrality of landing stations and cable density in contested waters.

### 2. Frontier AI Strategy (Geopolitical Intent)
- **Objective**: Map the expansion of "Frontier AI" and Hyperscale compute facilities.
- **Focus**: Detect where major powers (US, China) and corporations (Google, Microsoft, xAI) are positioning future compute capacity.
- **Insight**: Correlate data center builds with energy availability and geopolitical alignment.

### 3. Synthesis & Interdependency
- **Objective**: Understand the "Digital Supply Chain" from subsea cable -> landing station -> data center.
- **Focus**: How does new AI infrastructure rely on legacy maritime chokepoints? Where are the new critical nodes emerging?

## Project Structure
```text
atlas_gridwatch/
├── data/               # Data store (Raw, Processed, Outputs)
├── docs/               # Intelligence documentation (Methodology, Ethics)
├── scripts/            # ETL and Analysis pipelines
├── src/                # Core Python package
└── tests/              # Validation suite
```

## System Architecture
The platform operates as a cyclical intelligence pipeline:

1.  **Ingestion Layer**:
    - **OSINT Feeds**: Aggregates 30+ RSS sources (Maritime, Cyber, Tech, Geopolitics).
    - **Seed Data**: Critical infrastructure waypoints (Cables, Data Centers).
    - **Research Library**: Local repository of academic papers and PDF reports.
2.  **Persistence Layer**:
    - **News Database (SQLite)**: Archives all ingested articles with FTS5 for rapid retrieval.
    - **Master Graph (JSON)**: Network topology of global infrastructure.
3.  **Analysis Layer**:
    - **Graph Theory**: Calculates "Strategic Chokepoints" (Betweenness Centrality).
    - **AI Analyst (Gemini 2.0)**: Queries the News Database and Research Library to answer Priority Intelligence Requirements (PIRs).
4.  **Presentation Layer**:
    - **Interactive Map**: Leaflet.js visualization of the physical grid.
    - **Intelligence Brief**: Auto-generated HTML reports.

## Getting Started
## Getting Started

### Prerequisites
- Python 3.10+
- Google Cloud API Key (for Gemini 2.0)
- OpenAI API Key (Optional / Fallback)

### Installation
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/elchacal801/atlas_gridwatch.git
    cd atlas_gridwatch
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**
    Create a `.env` file in the root directory:
    ```env
    GOOGLE_API_KEY=your_gemini_key_here
    OPENAI_API_KEY=your_openai_key_here
    ```

### Usage

**1. Run the Intelligence Cycle (Ingestion)**
Fetch latest news and updates from data sources.
```bash
python scripts/ingestion/run_ingestion.py --source rss
```

**2. Generate Strategic Assessment**
Run the AI Analyst to synthesize data and generate the report.
```bash
python scripts/analysis/run_analysis.py
```

**3. View Results**
Open the generated brief in your browser:
- `data/outputs/ai_assessment.html`

## Ethics & Safety
This project adheres to strict OSINT guidelines. We do not aggregate PII, internal proprietary data, or targeting information. See `docs/ethics.md` for our full operational policy.
