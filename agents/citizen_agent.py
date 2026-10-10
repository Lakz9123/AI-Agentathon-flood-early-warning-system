import os
from agents.state import FloodSystemState
from database.database import get_recent_reports_count

def citizen_node(state: FloodSystemState) -> FloodSystemState:
    """Agent responsible for analyzing citizen reports."""
    location = state.get("location", "")
    demo_mode = state.get("demo_mode", False)
    
    if demo_mode and location.lower() == "chennai":
        count = 15
        baseline = 3.0
    else:
        # Fetch from SQLite database
        try:
            count, baseline = get_recent_reports_count(location)
        except Exception as e:
            count = 0
            baseline = 0.0
            
    state["citizen_data"] = {
        "complaints_count": count,
        "baseline_daily_avg": baseline,
        "unusual_increase": count > baseline * 1.5 if baseline > 0 else count > 5
    }
    return state
