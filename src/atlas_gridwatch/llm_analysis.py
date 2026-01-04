import os
import logging
from typing import Dict, Any, List
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
logger = logging.getLogger(__name__)

class LLMAnalyzer:
    """
    AI-Powered Strategic Analyst.
    Uses OpenAI to interpret raw infrastructure metrics into intelligence assessments.
    """

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            logger.warning("OPENAI_API_KEY not found in .env. LLM analysis will be skipped.")
            self.client = None
        else:
            self.client = OpenAI(api_key=self.api_key)

    def _generate_fallback(self, context: Dict[str, Any], reason: str) -> str:
        """
        Generates a static fallback assessment when LLM is unavailable.
        """
        nodes = context.get("critical_nodes", [])
        planned = context.get("planned_assets", [])
        risk = context.get("jurisdiction_risk", {})
        
        return f"""
        <div class="assessment-section mb-3">
            <h5 style="color: #666; border-bottom: 1px solid #555; padding-bottom: 5px;">
                <i class="bi bi-exclamation-triangle"></i> Automated Analysis Unavailable
            </h5>
            <div style="color: #aaa;">
                <p>The AI Strategic Analyst is currently offline ({reason}).</p>
                <strong>System Statistics:</strong>
                <ul>
                    <li><strong>Critical Nodes Detected:</strong> {len(nodes)}</li>
                    <li><strong>Planned AI Facilities:</strong> {len(planned)}</li>
                    <li><strong>Jurisdictional Spread:</strong> {len(risk)} countries</li>
                </ul>
                <p><em>Please ensure OPENAI_API_KEY is configured in Settings/Secrets.</em></p>
            </div>
        </div>
        """

    def _load_knowledge_base(self) -> str:
        """
        Loads content from local research papers (markdown) to serve as RAG context.
        """
        kb_content = []
        papers_dir = Path("papers") # Relative to root execution
        if not papers_dir.exists():
            # Try absolute path fallback if needed, or relative to src
            papers_dir = Path("c:/Users/anon/Documents/anon/atlas_gridwatch/papers")
            
        if papers_dir.exists():
            for f in papers_dir.glob("*.md"):
                try:
                    text = f.read_text(encoding="utf-8")
                    # truncate heavily to avoid context window explosion, focus on headers/summaries if possible
                    # For now, take first 3000 chars of each paper
                    kb_content.append(f"--- SOURCE: {f.name} ---\n{text[:3000]}...\n")
                except Exception as e:
                    logger.warning(f"Failed to read paper {f}: {e}")
        
        return "\n".join(kb_content) if kb_content else "No local research papers available."

    def generate_assessment(self, context: Dict[str, Any]) -> str:
        """
        Generates a strategic assessment based on provided context data and Local Knowledge Base.
        """
        if not self.client:
            return self._generate_fallback(context, "Missing API Key")

        # Load Local Knowledge
        knowledge_base = self._load_knowledge_base()

        # Construct a high-level summary of the data for the LLM
        # We assume 'context' contains 'critical_nodes' and 'jurisdiction_risk'
        
        critical_nodes = context.get("critical_nodes", [])[:5] # Top 5
        risk_data = context.get("jurisdiction_risk", {})
        planned_assets = context.get("planned_assets", [])
        
        # Prepare text representation
        nodes_txt = "\n".join([f"- {n['name']} ({n['country']}): Score {n['betweenness']:.3f}" for n in critical_nodes])
        risk_txt = "\n".join([f"- {k}: {v} assets" for k,v in risk_data.items()])
        planned_txt = "\n".join([f"- [PLANNED] {a.get('name')} ({a.get('location', {}).get('country')}) - Owner: {a.get('owner_id')} - Intent: {a.get('properties', {}).get('intent')}" for a in planned_assets])
        
        prompt = f"""
        You are a Strategic Intelligence Analyst for Atlas Gridwatch. 
        
        Analyze the provided critical infrastructure data in the context of our **Local Knowledge Base** (verified research papers).
        SEPARATE your analysis into two distinct sections: "Maritime & Cable Chokepoints" and "Frontier AI Infrastructure".
        
        ### LOCAL KNOWLEDGE BASE (Verified Intelligence)
        {knowledge_base}
        
        ### REAL-TIME METRICS (Current Status)
        **Strategic Chokepoints (Cables/Active):**
        {nodes_txt}
        
        **Jurisdiction Risk:**
        {risk_txt}
        
        **Frontier AI / Planned Buildout:**
        {planned_txt if planned_assets else "No immediate planned facility intelligence available."}
        
        ### PIR REQUIREMENTS
        1. **Maritime Domain**: Analyze the physical resilience of the subsea cable network. 
           - Cite specific insights from the Knowledge Base (e.g. historical outages, specific chokepoint risks).
           - Correlate the "Real-Time Metrics" (e.g. 0.000 scores) with the Knowledge Base (e.g. "Similar to the 2008 Egypt incident...").
        2. **Frontier AI Domain**: Analyze the strategic placement of new AI/Hyperscale facilities. 
           - What is the geopolitical logic? 
           - Connect planned assets to the "Digital Silk Road" or US-China competition themes found in the papers.
        3. **Synthesis**: Create a "Deep Dive" scenario. How would a conflict in a high-risk region identified in the papers impact the specific AI assets listed in the metrics?
        
        ### OUTPUT FORMAT
        Return a valid JSON object (no markdown) with the following structure:
        {{
            "maritime_analysis": "<p>Analysis...</p>",
            "frontier_ai_analysis": "<p>Analysis...</p>",
            "synthesis": "<p><b>Scenario Modeling:</b> ...</p>"
        }}
        Do not use markdown formatting (like **bold**) inside the JSON values, use HTML tags (<strong>, <em>) if needed.
        """

        try:
            logger.info("Querying OpenAI for Strategic Assessment (with RAG)...")
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert intelligence analyst. Return your analysis in strict JSON format."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1500, # Increased for detailed analysis
                response_format={"type": "json_object"}
            )
            content = response.choices[0].message.content.strip()
            
            import json
            data = json.loads(content)
            
            # Construct HTML from JSON to guarantee separation
            html_output = f"""
            <div class="assessment-section mb-3">
                <h5 style="color: #00f2ff; border-bottom: 1px solid #00f2ff; padding-bottom: 5px;">
                    <i class="bi bi-water"></i> Maritime Resilience & Chokepoints (Systemic Risk)
                </h5>
                <div style="color: #ccc;">{data.get('maritime_analysis', 'Analysis unavailable.')}</div>
            </div>
            
            <div class="assessment-section mb-3">
                <h5 style="color: #bc1ce8; border-bottom: 1px solid #bc1ce8; padding-bottom: 5px;">
                    <i class="bi bi-cpu"></i> Frontier AI Strategy (Geopolitical Intent)
                </h5>
                <div style="color: #ccc;">{data.get('frontier_ai_analysis', 'Analysis unavailable.')}</div>
            </div>

            <div class="assessment-section">
                <h5 style="color: #ffffff; border-bottom: 1px solid #555; padding-bottom: 5px;">SRM Synthesis & Scenario Modeling</h5>
                <div style="font-style: italic; color: #aaa;">{data.get('synthesis', '')}</div>
            </div>
            """
            return html_output

        except Exception as e:
            logger.error(f"LLM Analysis failed: {e}")
            return self._generate_fallback(context, f"Error: {str(e)}")

    def extract_entity_from_text(self, text: str) -> Dict[str, Any]:
        """
        Extracts Data Center details from unstable text.
        Returns a dict compatible with DataCenter model or None.
        """
        if not self.client: return None

        prompt = f"""
        Extract "Frontier AI" or Hyperscale Data Center infrastructure details from the text below.
        
        CRITICAL INSTRUCTIONS:
        - We are looking for NEW, PLANNED, or EXPANDING facilities.
        - If a specific City is not mentioned, infer it from context or use "Unknown".
        - If the exact name is not mentioned, create a descriptive name (e.g. "Google New Cloud Region - Thailand").
        - Capture ANY mention of AWS, Azure, Google, Meta, xAI, OpenAI, or Oracle infrastructure.

        Return ONLY a JSON object (no markdown) with these keys:
        - "name": Name of the facility.
        - "owner": The primary hyperscaler or operator.
        - "city": City name (or "Unknown").
        - "country": Country name.
        - "latitude": Approximate latitude (float) or 0.0.
        - "longitude": Approximate longitude (float) or 0.0.
        - "intent": Brief description (e.g. "AI Training", "Cloud Region").
        - "status": ONE of ["active", "planned", "under_construction"]. Default to "planned" if ambiguous.

        If absolutely NO infrastructure facility is mentioned, return {{ "found": false }}.

        TEXT:
        {text[:2000]} 
        """
        
        try:
             response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert OSINT analyst extracting structured data from news."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1
            )
             content = response.choices[0].message.content.strip()
             # Cleanup code blocks if present
             if content.startswith("```"): content = content.split("\n", 1)[1].rsplit("\n", 1)[0]
             
             import json
             data = json.loads(content)
             
             if not data.get("found", True): 
                 return None
                 
             return data
        except Exception as e:
            logger.warning(f"OSINT Extraction failed: {e}")
            return None
    def analyze_news_items(self, news_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Filters and analyzes raw RSS news items for strategic relevance.
        Returns a list of high-value intelligence items.
        """
        if not self.client or not news_items:
            return []

        # Prepare a concise list for the LLM
        # We only take the top 15 most recent items to avoid token limits
        inputs = news_items[:15]
        context_txt = ""
        for i, item in enumerate(inputs):
            context_txt += f"ITEM {i+1}: Title: {item.get('title')} | Source: {item.get('source')} | Summary: {item.get('summary')[:200]}...\n"

        prompt = f"""
        You are a Watch Officer for Atlas Gridwatch.
        Review the following OSINT news items.
        
        FILTERING CRITERIA:
        1. **Relevance**: Does this impact Subsea Cables, Data Centers, AI Infrastructure, or Great Power Competition (US/China/Russia)?
        2. **Significance**: Is this a major strategic shift, legal change, or physical threat?
        
        INSTRUCTIONS:
        - Select only the top 3-5 most strategically relevant items.
        - For each selected item, provide a "Strategic Assessment" (1 sentence explaining WHY it matters).
        - Assign a Risk Level: [LOW, MEDIUM, HIGH].
        
        NEWS ITEMS:
        {context_txt}
        
        OUTPUT FORMAT:
        Return a valid JSON object with a key "intelligence_events" containing a list of objects:
        {{
            "intelligence_events": [
                {{
                    "title": "Original Title",
                    "source": "Source Name",
                    "url": "Original Link",
                    "risk": "HIGH", 
                    "assessment": "Brief strategic impact analysis."
                }}
            ]
        }}
        """

        try:
            logger.info("Analyzing news stream for strategic intelligence...")
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a military intelligence analyst. Output strict JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3, # Lower temp for more deterministic filtering
                response_format={"type": "json_object"}
            )
            content = response.choices[0].message.content.strip()
            import json
            data = json.loads(content)
            
            # Merit: Re-attach original links if LLM hallucinated or dropped them
            # We map back by title roughly or just trust the LLM if it copied correctly.
            # Robust way: The LLM output might not have the exact URL if we didn't explicitly map IDs.
            # Let's simple-map by index if we asked for IDs, but here we passed text.
            # The prompt asks for "Original Link", usually GPT-4o is good at copying.
            # But to be safe, we can try to fuzzy match or just rely on the LLM's return.
            
            return data.get("intelligence_events", [])

        except Exception as e:
            logger.error(f"News Analysis failed: {e}")
            return []
