import random

# Predefined realistic datasets per district for DEMO mode
DISTRICT_DEMO_DATA = {
    "District 1 - Coastal Zone": {
        "weather": {"forecast_mm": 115, "status": "Coastal Gale & Heavy Surge"},
        "water": {"current_level_m": 6.85, "danger_level_m": 7.5, "trend": "Rapidly Rising"}
    },
    "District 2 - River Basin": {
        "weather": {"forecast_mm": 185, "status": "Torrential Monsoonal Downpour"},
        "water": {"current_level_m": 8.45, "danger_level_m": 8.0, "trend": "Exceeded Crest (Breach)"}
    },
    "District 3 - Lowland Zone": {
        "weather": {"forecast_mm": 68, "status": "Moderate Intermittent Rain"},
        "water": {"current_level_m": 4.90, "danger_level_m": 6.5, "trend": "Slowly Rising"}
    },
    "District 4 - Metro Basin": {
        "weather": {"forecast_mm": 142, "status": "Severe Urban Flash Storm"},
        "water": {"current_level_m": 7.60, "danger_level_m": 8.0, "trend": "Rapidly Rising"}
    },
    "District 5 - Industrial Zone": {
        "weather": {"forecast_mm": 95, "status": "Heavy Industrial Corridor Rain"},
        "water": {"current_level_m": 6.20, "danger_level_m": 7.0, "trend": "Rising"}
    }
}

def _resolve_district_key(location: str) -> str:
    loc_lower = (location or "").lower()
    for key in DISTRICT_DEMO_DATA.keys():
        if key.lower() in loc_lower or loc_lower in key.lower() or (f"district {loc_lower[-1]}" in key.lower() if loc_lower[-1:].isdigit() else False):
            return key
        # Check simple number match
        for num in ["1", "2", "3", "4", "5"]:
            if f"district {num}" in loc_lower and f"district {num}" in key.lower():
                return key
    return "District 4 - Metro Basin"

def get_weather_forecast(location: str, demo_mode=True):
    """Fetches area-specific weather forecast."""
    dist_key = _resolve_district_key(location)
    
    if demo_mode:
        data = DISTRICT_DEMO_DATA[dist_key]["weather"]
        return {"forecast_mm": data["forecast_mm"], "status": data["status"]}
    
    # Non-demo: Add dynamic variance based on district baseline
    base = DISTRICT_DEMO_DATA[dist_key]["weather"]["forecast_mm"]
    forecast = max(10, min(260, base + random.randint(-20, 25)))
    status = "Torrential Rain" if forecast > 150 else "Heavy Rain" if forecast > 100 else "Moderate Rain" if forecast > 50 else "Scattered Showers"
    return {"forecast_mm": forecast, "status": status}

def get_water_level(location: str, demo_mode=True):
    """Fetches area-specific current water level."""
    dist_key = _resolve_district_key(location)
    
    if demo_mode:
        data = DISTRICT_DEMO_DATA[dist_key]["water"]
        return {
            "current_level_m": data["current_level_m"],
            "danger_level_m": data["danger_level_m"],
            "trend": data["trend"]
        }
    
    # Non-demo: Add dynamic variance based on district baseline
    base = DISTRICT_DEMO_DATA[dist_key]["water"]["current_level_m"]
    danger = DISTRICT_DEMO_DATA[dist_key]["water"]["danger_level_m"]
    current = round(max(1.5, min(danger + 1.2, base + random.uniform(-0.4, 0.5))), 2)
    trend = "Rapidly Rising" if current >= danger * 0.9 else "Rising" if current >= danger * 0.7 else "Stable"
    return {"current_level_m": current, "danger_level_m": danger, "trend": trend}
