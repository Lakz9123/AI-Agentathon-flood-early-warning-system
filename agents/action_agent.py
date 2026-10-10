import os
from langchain_google_genai import ChatGoogleGenerativeAI
from agents.state import FloodSystemState

def action_node(state: FloodSystemState) -> FloodSystemState:
    """Agent responsible for generating the prevention action plan using Gemini."""
    
    weather_data = state.get("weather_data", {})
    water_data = state.get("water_data", {})
    citizen_data = state.get("citizen_data", {})
    historical_data = state.get("historical_data", {})
    risk_assessment = state.get("risk_assessment", {})
    
    # Check if Gemini API key is available
    api_key = os.getenv("GEMINI_API_KEY")
    
    def generate_heuristic_plan(loc, score, cat, rain, water_cur, water_dang, complaints):
        actions = []
        if score >= 70:
            actions.append("- **Deploy automated pneumatic flood barricades** at low-lying arterial underpasses and canal gateways.")
            actions.append("- **Initiate high-capacity stormwater pumps** to evacuate excess channel volume before surge peak.")
            actions.append("- **Broadcast Level 3 Flash Flood Advisory** via municipal emergency broadcast mesh to vulnerable wards.")
            actions.append("- **Mobilize civil protection search & rescue flotilla** to forward staging outposts.")
            priority = "Critical (DEFCON 1/2)"
        elif score >= 40:
            actions.append("- **Clear primary canal drainage grates** and remove debris blockages reported by citizens.")
            actions.append("- **Pre-position mobile diesel pump trailers** near monitored drainage choke points.")
            actions.append("- **Issue precautionary traffic rerouting notice** for flood-prone transit corridors.")
            priority = "High (DEFCON 3)"
        else:
            actions.append("- **Maintain standard hydrological telemetry telemetry monitoring** across regional sensor mesh.")
            actions.append("- **Conduct routine inspection of culverts** and retain normal weir discharge levels.")
            priority = "Low (DEFCON 4)"
            
        plan = f"""### Tactical Decision-Support Recommendations
**Priority Level**: {priority}
**Target Sector**: {loc}

#### Immediate Actions:
""" + "\n".join(actions) + f"""

#### Recommended Authorities:
- Municipal Corporation Disaster Cell & Public Works (PWD)
- State Disaster Management Authority (SDMA)
- Regional Traffic Police Dispatch

*(Decision-support suggestions for responsible authorities. Verified by Sentinel AI Rules Engine)*"""
        return plan

    if not api_key or api_key == "your_gemini_api_key_here":
        state["action_plan"] = generate_heuristic_plan(
            state.get('location', 'Sector'),
            risk_assessment.get('score', 50),
            risk_assessment.get('category', 'MEDIUM'),
            weather_data.get('forecast_mm', 0),
            water_data.get('current_level_m', 0),
            water_data.get('danger_level_m', 8.0),
            citizen_data.get('complaints_count', 0)
        )
        return state

    try:
        # Initialize Gemini LLM
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
        
        prompt = f"""
        You are Sentinel AI, an expert Disaster Management Assistant.
        Analyze the following data and provide a concise, prioritized flood prevention plan.
        
        DATA:
        - Location: {state.get('location')}
        - Rainfall forecast: {weather_data.get('forecast_mm')} mm
        - Water level: {water_data.get('current_level_m')} / {water_data.get('danger_level_m')} m (Trend: {water_data.get('trend')})
        - Citizen complaints: {citizen_data.get('complaints_count')}
        - Historical flood risk: {historical_data.get('historical_risk')}
        - Overall risk score: {risk_assessment.get('score')} ({risk_assessment.get('category')})
        
        Format your output nicely with markdown.
        Include:
        1. Immediate Actions (bullet points with strong verbs, each starting with -)
        2. Priority Level (Critical / High / Medium / Low)
        3. Recommended Authorities to involve
        
        IMPORTANT: Do not generate medical, evacuation, or emergency instructions as authoritative orders. 
        Clearly label recommendations as "Decision-support suggestions for responsible authorities".
        Keep the response brief and highly readable.
        """
        
        response = llm.invoke(prompt)
        state["action_plan"] = response.content
        
    except Exception as e:
        print(f"Gemini API Error: {e}")
        state["action_plan"] = generate_heuristic_plan(
            state.get('location', 'Sector'),
            risk_assessment.get('score', 50),
            risk_assessment.get('category', 'MEDIUM'),
            weather_data.get('forecast_mm', 0),
            water_data.get('current_level_m', 0),
            water_data.get('danger_level_m', 8.0),
            citizen_data.get('complaints_count', 0)
        )
        
    return state
