from typing import TypedDict, List, Dict, Any

class FloodSystemState(TypedDict):
    # Inputs
    location: str
    demo_mode: bool
    
    # Agent Outputs
    weather_data: Dict[str, Any]
    water_data: Dict[str, Any]
    citizen_data: Dict[str, Any]
    historical_data: Dict[str, Any]
    
    # Final Computed Risk
    risk_assessment: Dict[str, Any]
    
    # Action Plan
    action_plan: str
