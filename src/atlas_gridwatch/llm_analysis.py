import os
import logging
from typing import Dict, Any, List
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

    def generate_assessment(self, context: Dict[str, Any]) -> str:
        """
        Generates a strategic assessment based on provided context data.
        """
        if not self.client:
            return "<!-- AI Assessment Unavailable: Missing API Key -->"

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
        
        Analyze the provided critical infrastructure data.
        SEPARATE your analysis into two distinct sections: "Maritime & Cable Chokepoints" and "Frontier AI Infrastructure".

        ### INTELLIGENCE DATA
        **Strategic Chokepoints (Cables/Active):**
        {nodes_txt}

        **Jurisdiction Risk:**
        {risk_txt}
        
        **Frontier AI / Planned Buildout:**
        {planned_txt if planned_assets else "No immediate planned facility intelligence available."}

        ### PIR REQUIREMENTS
        1. **Maritime Domain**: Analyze the physical resilience of the subsea cable network. Identify top chokepoints.
        2. **Frontier AI Domain**: Analyze the strategic placement of new AI/Hyperscale facilities. What is the geopolitical logic behind these specific locations?
        3. **Synthesis**: How does the new AI infrastructure rely on the existing cable vulnerabilities?

        ### OUTPUT FORMAT
        Return a valid JSON object (no markdown) with the following structure:
        {{
            "maritime_analysis": "<p>Analysis of cables...</p><ul><li>...</li></ul>",
            "frontier_ai_analysis": "<p>Analysis of AI location strategy...</p>",
            "synthesis": "<p>Executive summary...</p>"
        }}
        Do not use markdown formatting (like **bold**) inside the JSON values, use HTML tags (<strong>, <em>) if needed.
        """

        try:
            logger.info("Querying OpenAI for Strategic Assessment...")
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert intelligence analyst. Return your analysis in strict JSON format."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=800,
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
                <h5 style="color: #ffffff; border-bottom: 1px solid #555; padding-bottom: 5px;">SRM Synthesis</h5>
                <div style="font-style: italic; color: #aaa;">{data.get('synthesis', '')}</div>
            </div>
            """
            return html_output

        except Exception as e:
            logger.error(f"LLM Analysis failed: {e}")
            return f"<!-- AI Assessment Failed: {e} -->"

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
