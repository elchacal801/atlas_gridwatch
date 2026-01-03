# Analytical Methodology

Atlas Gridwatch applies the classic **Intelligence Cycle** to infrastructure mapping.

## 1. Direction (The Question)
We start with a strategic question.
*   *Example: "Where is the physical center of gravity for AI compute shifting in the next 3 years?"*
*   *Example: "What are the single points of failure for trans-Atlantic data capability?"*

## 2. Collection (The Data)
We ingest data from diverse, open sources.
*   **Physical Layer**: Data center locations, power grid maps, fiber routes.
*   **Logical Layer**: BGP routing, IXP memberships, peering relationships.
*   **Corporate Layer**: Ownership structures, subsidiaries, investment announcements.

## 3. Processing (Normalization)
Raw data is messy. We normalize it into a unified schema:
*   **Geocoding**: Converting addresses to Lat/Long.
*   **Entity Resolution**: Mapping "Google", "Alphabet", and shell companies to a single canonical entity.
*   **Temporal Tagging**: Assigning valid-from/valid-to dates to infrastructure status.

## 4. Analysis (Enrichment)
We apply analytical techniques to the clean data.
*   **Clustering**: Identifying high-density zones.
*   **Graph Analysis**: Measuring centrality and connectivity.
*   **Gap Analysis**: Identifying missing or contradictory data.

## 5. Dissemination (Visualization)
We present findings in high-signal formats.
*   Maps are for *spatial* context.
*   Graphs are for *relational* context.
*   Briefs are for *strategic* context.
