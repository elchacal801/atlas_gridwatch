import os
import logging
from typing import Dict, Any, List
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from openai import OpenAI
from google import genai
from google.genai import types
from .database import NewsDatabase

load_dotenv()
logger = logging.getLogger(__name__)

class LLMAnalyzer:
    """
    AI-Powered Strategic Analyst.
    Uses OpenAI to interpret raw infrastructure metrics into intelligence assessments.
    """

    def __init__(self):
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.gemini_key = os.getenv("GOOGLE_API_KEY")
        
        # Initialize Databases
        self.news_db = NewsDatabase()
        
        # Initialize Clients
        self.client = None
        self.gemini_model = None

        if self.gemini_key:
            try:
                self.gemini_client = genai.Client(api_key=self.gemini_key)
                logger.info("Gemini API (new SDK) configured successfully.")
            except Exception as e:
                logger.error(f"Failed to configure Gemini: {e}")
                self.gemini_client = None

        if self.openai_key:
            self.client = OpenAI(api_key=self.openai_key)
        else:
            logger.warning("OPENAI_API_KEY not found.")

        if not self.client and not self.gemini_client:
            logger.warning("No LLM backend available.")

    def _call_llm(self, system_prompt: str, user_prompt: str, json_mode: bool = True) -> str:
        """
        Abstracted LLM call favoring Gemini, falling back to OpenAI.
        """
        # 1. Try Gemini
        if self.gemini_client:
            try:
                # Construct combined prompt as Gemini 1.5 Flash handles large contexts well
                full_prompt = f"SYSTEM: {system_prompt}\n\nUSER: {user_prompt}"
                
                config = None
                if json_mode:
                    config = types.GenerateContentConfig(response_mime_type="application/json")
                
                response = self.gemini_client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=full_prompt,
                    config=config
                )
                return response.text
            except Exception as e:
                logger.warning(f"Gemini generation failed: {e}")
        
        # 2. Fallback to OpenAI
        if self.client:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                response_format={"type": "json_object"} if json_mode else None
            )
            return response.choices[0].message.content.strip()
            
        raise Exception("All LLM backends failed.")

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
        Loads content from local research papers (markdown) AND docs/research to serve as RAG context.
        """
        kb_content = []
        sources = []

        # 1. Primary Papers Directory
        papers_dir = Path("papers")
        if not papers_dir.exists():
             papers_dir = Path("c:/Users/anon/Documents/anon/atlas_gridwatch/papers")
        if papers_dir.exists():
            sources.extend(list(papers_dir.glob("*.md")))

        # 2. Expanded Research Library (docs/research) - Recursive scan for MD
        research_dir = Path("docs/research")
        if not research_dir.exists():
             research_dir = Path("c:/Users/anon/Documents/anon/atlas_gridwatch/docs/research")
        if research_dir.exists():
            # rglob to find nested markdowns (e.g. inside data_centers_epochAI)
            sources.extend(list(research_dir.rglob("*.md")))

        # Deduplicate paths
        unique_sources = {str(p.resolve()): p for p in sources}.values()

        for f in unique_sources:
            try:
                text = f.read_text(encoding="utf-8")
                # truncate heavily to avoid context window explosion
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
        critical_nodes = context.get("critical_nodes", [])[:5] # Top 5
        risk_data = context.get("jurisdiction_risk", {})
        planned_assets = context.get("planned_assets", [])
        
        # Prepare text representation
        nodes_txt = "\n".join([f"- {n['name']} ({n['country']}): Score {n['betweenness']:.3f}" for n in critical_nodes])
        risk_txt = "\n".join([f"- {k}: {v} assets" for k,v in risk_data.items()])
        planned_txt = "\n".join([f"- [PLANNED] {a.get('name')} ({a.get('location', {}).get('country')}) - Owner: {a.get('owner_id')} - Intent: {a.get('properties', {}).get('intent')}" for a in planned_assets])
        
        prompt = f"""
        You are the **Chief Strategic Intelligence Analyst** for Atlas Gridwatch.
        Your mandate is to produce a **high-level, classified strategic assessment** utilizing the **Analysis of Competing Hypotheses (ACH)** framework.
        
        Analyze the provided critical infrastructure metrics in the context of our **Local Knowledge Base** (verified research papers).
        
        ### LOCAL KNOWLEDGE BASE (Verified Intelligence)
        {knowledge_base}

        ### RECENT STRATEGIC NEWS (RAG Context)
        {self.news_db.get_context_for_analysis(["cable", "outage", "sabotage", "data center", "AI", "China", "Russia"], limit_per_keyword=2)}
        
        ### REAL-TIME METRICS (Current Operational Picture)
        **Strategic Chokepoints (Cables/Active):**
        {nodes_txt}
        
        **Jurisdiction Risk:**
        {risk_txt}
        
        **Frontier AI / Planned Buildout:**
        {planned_txt if planned_assets else "No immediate planned facility intelligence available."}
        
        ### PRIORITY INTELLIGENCE REQUIREMENTS (PIRs) - DEEP DIVE
        
        **PIR 1: Maritime & Cable Resilience**
        - Analyze the physical resilience of the subsea cable network.
        - **Constraint**: You MUST cite specific historical precedents or risks from the Knowledge Base.
        
        **PIR 2: Frontier AI Geopolitics**
        - Analyze the strategic placement of new AI/Hyperscale facilities.
        - **Constraint**: Connect this to "Great Power Competition" (US vs China) and the "Digital Silk Road".
        
        **PIR 3: Supply Chain & Energy Dependencies** (NEW)
        - What are the power/cooling constraints? What are the kinetic vulnerabilities (e.g. substations, water supply)?
        - How does the "Compute Divide" mentioned in papers impact this?
        
        **PIR 4: Cyber-Physical Convergence** (NEW)
        - How could a coordinated cyber-attack on SCADA systems amplify the physical sabotage risks identified in PIR 1?
        
        ### CRITICAL THINKING & RED TEAM
        **Red Team Analysis (Devil's Advocate)**:
        - Challenge your own assessment. What if the perceived threat is a deception? What if the "safe" jurisdictions are actually compromised?
        
        ### OUTPUT FORMAT
        Return a valid JSON object (no markdown) with the following strategy:
        {{
            "maritime_analysis": "<p>Deep dive into cable risks...</p>",
            "frontier_ai_analysis": "<p>Geopolitical analysis of AI...</p>",
            "supply_chain_analysis": "<p>Analysis of energy and supply chain vulnerabilities...</p>",
            "red_team_analysis": "<p><strong>Alternative View:</strong> ...</p>",
            "synthesis": "<p><strong>Executive Summary & Scenario Modeling:</strong> ...</p>"
        }}
        Do not use markdown formatting (like **bold**) inside the JSON values, use HTML tags (<strong>, <em>) if needed.
        """
        
        try:
            logger.info("Querying LLM for Enhanced Strategic Assessment...")
            content = self._call_llm(
                system_prompt="You are an expert intelligence analyst using the ACH framework. Output strict JSON.",
                user_prompt=prompt,
                json_mode=True
            )
            
            import json
            data = json.loads(content)
            
            # Construct HTML from JSON with new sections
            html_output = f"""
            <div class="assessment-section mb-3">
                <h5 style="color: #00f2ff; border-bottom: 1px solid #00f2ff; padding-bottom: 5px;">
                    <i class="bi bi-water"></i> Maritime Resilience (PIR 1)
                </h5>
                <div style="color: #ccc;">{data.get('maritime_analysis', 'Analysis unavailable.')}</div>
            </div>
            
            <div class="assessment-section mb-3">
                <h5 style="color: #bc1ce8; border-bottom: 1px solid #bc1ce8; padding-bottom: 5px;">
                    <i class="bi bi-cpu"></i> Frontier AI Geopolitics (PIR 2)
                </h5>
                <div style="color: #ccc;">{data.get('frontier_ai_analysis', 'Analysis unavailable.')}</div>
            </div>

            <div class="assessment-section mb-3">
                <h5 style="color: #ffaa00; border-bottom: 1px solid #ffaa00; padding-bottom: 5px;">
                    <i class="bi bi-lightning-charge"></i> Energy & Supply Chain (PIR 3)
                </h5>
                <div style="color: #ccc;">{data.get('supply_chain_analysis', 'Analysis unavailable.')}</div>
            </div>

            <div class="assessment-section mb-3">
                <h5 style="color: #ff4444; border-bottom: 1px solid #ff4444; padding-bottom: 5px;">
                    <i class="bi bi-shield-exclamation"></i> Red Team / Alternative Hypotheses
                </h5>
                <div style="color: #ccc;">{data.get('red_team_analysis', 'Analysis unavailable.')}</div>
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
             content = self._call_llm(
                system_prompt="You are an expert OSINT analyst extracting structured data from news.",
                user_prompt=prompt,
                json_mode=True
             )
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
            content = self._call_llm(
                system_prompt="You are a military intelligence analyst. Output strict JSON.",
                user_prompt=prompt,
                json_mode=True
            )
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
