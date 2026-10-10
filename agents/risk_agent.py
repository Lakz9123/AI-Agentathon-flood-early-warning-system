from agents.state import FloodSystemState
from utils.risk_calculator import calculate_risk_score

def risk_node(state: FloodSystemState) -> FloodSystemState:
    """Agent responsible for combining signals and calculating risk score."""
    weather_data = state.get("weather_data", {})
    water_data = state.get("water_data", {})
    citizen_data = state.get("citizen_data", {})
    historical_data = state.get("historical_data", {})
    
    assessment = calculate_risk_score(weather_data, water_data, citizen_data, historical_data)
    
    state["risk_assessment"] = assessment
    return state
