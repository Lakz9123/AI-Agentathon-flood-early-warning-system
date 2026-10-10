import os
from agents.state import FloodSystemState
from database.database import get_recent_reports_count

def citizen_node(state: FloodSystemState) -> FloodSystemState:
    """Agent responsible for analyzing citizen reports."""
    location = state.get("location", "")
    demo_mode = state.get("demo_mode", False)
    
    if demo_mode and location == "Chennai":
        count = 15
    else:
        # Fetch from SQLite database
        try:
            count = get_recent_reports_count(location)
        except Exception as e:
            count = 0
            
    state["citizen_data"] = {"complaints_count": count}
    return state
