from agents.state import FloodSystemState
from utils.api_utils import get_water_level

def water_node(state: FloodSystemState) -> FloodSystemState:
    """Agent responsible for monitoring water levels."""
    location = state.get("location", "")
    demo_mode = state.get("demo_mode", False)
    
    # Fetch water level data
    water_data = get_water_level(location, demo_mode)
    
    # Update state
    state["water_data"] = water_data
    return state
