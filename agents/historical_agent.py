import os
import json
import pandas as pd
from agents.state import FloodSystemState

JSON_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "historical_districts.json")
CSV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "historical_flood_data.csv")

def get_historical_data(location: str) -> dict:
    # First check structured district JSON
    if os.path.exists(JSON_PATH):
        try:
            with open(JSON_PATH, "r", encoding="utf-8") as f:
                districts = json.load(f)
            
            # Match by exact name or substring
            for dist_name, dist_info in districts.items():
                if dist_name.lower() in location.lower() or location.lower() in dist_name.lower():
                    # Return summary and historical risk tier
                    tot_events = dist_info.get("total_events", 15)
                    hist_risk = "High" if tot_events >= 18 else "Medium" if tot_events >= 14 else "Moderate"
                    return {
                        "previous_flood_events": tot_events,
                        "historical_risk": hist_risk,
                        "avg_annual_rainfall_mm": dist_info.get("avg_annual_rainfall_mm", 1300),
                        "max_recorded_water_m": dist_info.get("max_recorded_water_m", 7.5),
                        "most_severe_event": dist_info.get("most_severe_event", "Seasonal Surge"),
                        "trend": dist_info.get("trend", "Upward")
                    }
        except Exception:
            pass

    # Fallback to CSV
    try:
        df = pd.read_csv(CSV_PATH)
        row = df[df['location'].str.lower() == location.lower()]
        if not row.empty:
            return {
                "previous_flood_events": int(row.iloc[0]['previous_flood_events']),
                "historical_risk": row.iloc[0]['historical_risk']
            }
    except Exception:
        pass
        
    return {"previous_flood_events": 15, "historical_risk": "Medium"}

def historical_node(state: FloodSystemState) -> FloodSystemState:
    """Agent responsible for checking historical flood risk for the selected area."""
    location = state.get("location", "District 4 - Metro Basin")
    demo_mode = state.get("demo_mode", False)
    
    if demo_mode and location.lower() == "chennai":
        hist_data = {"previous_flood_events": 3, "historical_risk": "High"}
    else:
        hist_data = get_historical_data(location)
    state["historical_data"] = hist_data
    return state
