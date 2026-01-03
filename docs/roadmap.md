# Atlas Gridwatch Strategic Roadmap

Based on our mission to providing **Strategic Intelligence on Global Compute & Connectivity Infrastructure**, this roadmap outlines the evolution of the platform into a comprehensive monitoring system.

## Phase 1: Automated News Intelligence (Immediate Priority)
**Objective**: Transform the platform from a static map into a living, breathing intelligence dashboard.

-   **Continuous Monitoring**:
    -   Implement GitHub Actions to run `run_ingestion.py` and `run_analysis.py` on a daily schedule (00:00 UTC).
    -   Expand `RSSIngestor` to cover detailed sources:
        -   **Tech**: Data Center Dynamics, Submarine Telecoms Forum.
        -   **Geopolitics**: War on the Rocks, CSIS, Foreign Policy (via available feeds).
        -   **National Security**: Defense One, C4ISRNET.
-   **AI News Analysis**:
    -   Upgrade `LLMAnalyzer` to process news items specifically for:
        -   **Strategic Relevance**: "Does this impact our chokepoints?"
        -   **Risk Assessment**: "Does this increase the risk score of a jurisdiction?"
    -   Generate a "Daily Briefing" section in the HTML report.
-   **Ticker/Feed UI**:
    -   Add a scrolling news ticker or a dedicated "Latest Intelligence" sidebar to the dashboard.

## Phase 2: Advanced Geospatial Layers (Medium Term)
**Objective**: Add depth to the analysis by correlating infrastructure with critical dependencies.

-   **Energy Grid Layer**:
    -   Map high-voltage transmission lines and power plants (Nuclear/Hydro) near Frontier AI clusters.
    -   Use `OpenInfrastructureMap` data.
-   **Political Stability Layer**:
    -   Overlay "Fragile States Index" or similar metrics onto Jurisdictions.
    -   Heatmap of "High Risk" zones for data integrity.
-   **Naval Chokepoint Zones**:
    -   Explicit polygons for Straits of Malacca, Hormuz, Suez.
    -   Alert logic: "New Cable planned through High Conflict Zone."

## Phase 3: Recursive Analysis & War Gaming (Long Term)
**Objective**: Move from descriptive to predictive intelligence.

-   **"What If?" Scenarios**:
    -   LLM-driven simulation: "If the Luzon Strait is blockaded, calculate % of data traffic rerouted."
-   **Entity Resolution Graph**:
    -   Build a graph database (Neo4j or NetworkX persistent) linking Shell Companies -> Owners -> Nation States.
-   **Satellite Verification**:
    -   Integrate Sentinel-2 API to watch for construction progress at identified "Planned" sites.

## Phase 4: Enterprise/Gov Integration
-   **API Export**: Serve `infrastructure_master.json` as a secure API endpoint.
-   **STIX/TAXII Support**: Export threat intelligence in standard formats for integration with SOC/Cyber command centers.
