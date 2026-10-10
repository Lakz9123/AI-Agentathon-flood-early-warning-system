from agents.state import FloodSystemState
from utils.api_utils import get_weather_forecast

def weather_node(state: FloodSystemState) -> FloodSystemState:
    """Agent responsible for checking weather conditions."""
    location = state.get("location", "")
    demo_mode = state.get("demo_mode", False)
    
    # Fetch weather data
    weather_data = get_weather_forecast(location, demo_mode)
    
    # Update state
    state["weather_data"] = weather_data
    return state
