from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

from agents.workflow import build_workflow
from database.database import init_db, insert_report, get_reports_by_location

app = FastAPI(title="Sentinel AI API")

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize the Database
init_db()

@app.get("/", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="dashboard.html")

@app.get("/citizen-report", response_class=HTMLResponse)
async def get_citizen_report(request: Request):
    return templates.TemplateResponse(request=request, name="citizen_report.html")

@app.get("/historical", response_class=HTMLResponse)
async def get_historical(request: Request):
    return templates.TemplateResponse(request=request, name="historical.html")

@app.get("/about", response_class=HTMLResponse)
async def get_about(request: Request):
    return templates.TemplateResponse(request=request, name="about.html")

@app.get("/map", response_class=HTMLResponse)
async def get_map(request: Request):
    return templates.TemplateResponse(request=request, name="map.html")

@app.get("/risk", response_class=HTMLResponse)
async def get_risk(request: Request):
    return templates.TemplateResponse(request=request, name="risk.html")

@app.post("/api/analyze")
async def analyze_flood_risk(request: Request):
    """
    Trigger the LangGraph workflow to perform multi-agent analysis.
    """
    data = await request.json()
    location = data.get("location", "Chennai")
    demo_mode = data.get("demo_mode", False)

    workflow = build_workflow()
    initial_state = {
        "location": location,
        "demo_mode": demo_mode,
        "weather_data": {},
        "water_data": {},
        "citizen_data": {},
        "historical_data": {},
        "risk_assessment": {},
        "action_plan": ""
    }
    
    final_state = initial_state
    for output in workflow.stream(initial_state):
        for key, value in output.items():
            final_state.update(value)
            
    # Include both snake_case and nested keys for backward and forward compatibility
    weather = final_state.get("weather_data", {})
    water = final_state.get("water_data", {})
    risk = final_state.get("risk_assessment", {})
    score = risk.get("score", 0)
    
    defcon = "DEFCON 1 (CRITICAL)" if score >= 80 else "DEFCON 2 (HIGH)" if score >= 60 else "DEFCON 3 (MODERATE)" if score >= 40 else "DEFCON 4 (NORMAL)"
    
    final_state["weather"] = {
        "precipitation_mm": weather.get("forecast_mm", 0),
        "status": weather.get("status", "Normal")
    }
    final_state["water"] = {
        "water_level_m": water.get("current_level_m", 0),
        "danger_level_m": water.get("danger_level_m", 8.0),
        "trend": water.get("trend", "Stable")
    }
    final_state["defcon"] = defcon
    
    return JSONResponse(content=final_state)

@app.get("/api/telemetry")
async def get_telemetry(location: str = "Chennai", demo_mode: bool = False):
    from utils.api_utils import get_weather_forecast, get_water_level
    from database.database import get_recent_reports_count
    
    weather = get_weather_forecast(location, demo_mode)
    water = get_water_level(location, demo_mode)
    complaints = get_recent_reports_count(location)
    
    return JSONResponse(content={
        "location": location,
        "precipitation_mm": weather.get("forecast_mm", 0),
        "weather_status": weather.get("status", "Clear"),
        "water_level_m": water.get("current_level_m", 0),
        "danger_level_m": water.get("danger_level_m", 8.0),
        "trend": water.get("trend", "Stable"),
        "complaints_count": complaints
    })

@app.post("/api/report")
async def submit_report(
    name: str = Form(""), 
    location: str = Form(...), 
    issue_type: str = Form(...), 
    severity: str = Form(...), 
    description: str = Form("")
):
    insert_report(name, location, issue_type, severity, description)
    return JSONResponse(content={"status": "success", "message": "Citizen report logged into database."})

@app.get("/api/reports")
@app.get("/api/reports/{location}")
async def fetch_reports(location: str = None):
    import sqlite3
    from database.database import DB_PATH
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if location and location.lower() != "all":
        cursor.execute('SELECT * FROM citizen_reports WHERE location = ? ORDER BY timestamp DESC LIMIT 20', (location,))
    else:
        cursor.execute('SELECT * FROM citizen_reports ORDER BY timestamp DESC LIMIT 20')
    reports = cursor.fetchall()
    conn.close()
    
    report_list = [
        {
            "id": r[0], "name": r[1] or "Anonymous Citizen", "location": r[2], 
            "issue_type": r[3], "severity": r[4], 
            "description": r[5], "timestamp": r[6]
        } for r in reports
    ]
    return JSONResponse(content={"reports": report_list})

@app.post("/api/dispatch")
async def dispatch_signal(request: Request):
    data = await request.json()
    hazard = data.get("hazard", "Rapid Surge Inundation")
    sector = data.get("sector", "Sector 4B - Metro Basin")
    return JSONResponse(content={
        "status": "success",
        "message": f"Signal successfully dispatched to EOC & Civil Protection Units for {sector}.",
        "hazard": hazard,
        "dispatch_id": "DSP-" + str(os.urandom(3).hex()).upper()
    })

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
