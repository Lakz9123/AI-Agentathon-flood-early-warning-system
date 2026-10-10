import streamlit as st
from dotenv import load_dotenv
import pandas as pd
import os
import time
from streamlit_folium import st_folium

# Import project modules
from agents.workflow import build_workflow
from database.database import init_db, insert_report, get_reports_by_location
from visualizations.charts import create_risk_gauge, create_rainfall_chart, create_water_level_chart, create_citizen_complaints_chart
from visualizations.map import create_flood_map

# Load environment variables
load_dotenv()

# Initialize DB
init_db()

# Configure page
st.set_page_config(
    page_title="Sentinel AI - Command Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Global CSS Injection ---
st.markdown("""
<style>
/* Dark slate navy background */
.stApp {
    background-color: #0B0E14 !important;
    color: #E2E8F0 !important;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}
/* Monospace for metric values */
.stMetric value {
    font-family: 'Courier New', monospace !important;
    color: #00F2FE !important;
}
/* Sidebar glassmorphism */
[data-testid="stSidebar"] {
    background-color: rgba(15, 23, 42, 0.9) !important;
    backdrop-filter: blur(10px);
    border-right: 1px solid rgba(0, 242, 254, 0.2);
}
/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #E2E8F0 !important;
}
/* Custom Metric Cards */
.glass-card {
    background-color: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(0, 242, 254, 0.15);
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5), 0 2px 4px -1px rgba(0, 0, 0, 0.3);
}
.glass-card h4 {
    color: #94A3B8;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 0;
    margin-bottom: 10px;
}
.glass-value {
    font-family: 'Courier New', monospace;
    font-size: 2.5rem;
    color: #00F2FE;
    font-weight: 700;
    margin: 0;
    text-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
}
.glass-sub {
    color: #64748B;
    font-size: 0.8rem;
    margin-top: 5px;
}
.risk-high {
    color: #EF4444 !important;
    text-shadow: 0 0 10px rgba(239, 68, 68, 0.5) !important;
}
.risk-medium {
    color: #F59E0B !important;
}
.risk-low {
    color: #10B981 !important;
}
/* Pipeline steps */
.pipeline-step {
    padding: 10px 15px;
    border-left: 2px solid #334155;
    margin-bottom: 10px;
    background-color: rgba(0,0,0,0.2);
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
    position: relative;
}
.pipeline-step.active {
    border-left-color: #00F2FE;
    background-color: rgba(0, 242, 254, 0.05);
}
.pipeline-step::before {
    content: '';
    position: absolute;
    left: -6px;
    top: 50%;
    transform: translateY(-50%);
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: #334155;
}
.pipeline-step.active::before {
    background-color: #00F2FE;
    box-shadow: 0 0 8px #00F2FE;
}
/* Buttons */
.stButton>button {
    background-color: transparent !important;
    color: #00F2FE !important;
    border: 1px solid #00F2FE !important;
    border-radius: 4px;
    transition: all 0.3s ease;
    font-family: 'Courier New', monospace !important;
    text-transform: uppercase;
}
.stButton>button:hover {
    background-color: rgba(0, 242, 254, 0.1) !important;
    box-shadow: 0 0 15px rgba(0, 242, 254, 0.3) !important;
}
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if 'workflow_state' not in st.session_state:
    st.session_state.workflow_state = None
if 'demo_mode' not in st.session_state:
    st.session_state.demo_mode = False
if 'location' not in st.session_state:
    st.session_state.location = "Chennai"

# --- Sidebar ---
st.sidebar.markdown("<h2 style='color: #00F2FE; font-family: monospace;'>SENTINEL AI</h2>", unsafe_allow_html=True)
st.sidebar.caption("AUTONOMOUS FLOOD DEFENSE ARCHITECTURE")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "SYSTEM MODULES", 
    ["Command Dashboard", "Citizen Report", "Historical Data", "About Project"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("<span style='color: #94A3B8; font-size: 0.8rem; text-transform: uppercase;'>Telemetry Target</span>", unsafe_allow_html=True)
locations = ["Chennai", "Mumbai", "Bangalore", "Delhi", "Pune", "Hyderabad"]
st.session_state.location = st.sidebar.selectbox("Location", locations, index=0, label_visibility="collapsed")

st.sidebar.markdown("<br>", unsafe_allow_html=True)
demo_toggle = st.sidebar.toggle("SIMULATION MODE (DEMO)", value=st.session_state.demo_mode)
st.session_state.demo_mode = demo_toggle

# --- Helper function to run agents ---
def run_analysis():
    workflow = build_workflow()
    initial_state = {
        "location": st.session_state.location,
        "demo_mode": st.session_state.demo_mode,
        "weather_data": {},
        "water_data": {},
        "citizen_data": {},
        "historical_data": {},
        "risk_assessment": {},
        "action_plan": ""
    }
    
    status_placeholder = st.empty()
    
    # Run the graph
    final_state = initial_state
    for output in workflow.stream(initial_state):
        for key, value in output.items():
            final_state.update(value)
            
            # Generate the pipeline visual
            steps = ["weather_data", "water_data", "citizen_data", "historical_data", "risk_assessment", "action_plan"]
            labels = ["Meteorological Sync", "Hydro-gauge Sync", "Citizen Signals", "Historical Records", "Risk Synthesis", "Intervention Plan"]
            
            html = ""
            for i, step in enumerate(steps):
                is_active = step in final_state and final_state[step]
                active_class = "active" if is_active else ""
                status_text = "COMPLETED" if is_active else "PENDING"
                color = "#00F2FE" if is_active else "#64748B"
                html += f"""
                <div class='pipeline-step {active_class}'>
                    <div style="display: flex; justify-content: space-between;">
                        <span>{labels[i]}</span>
                        <span style="color: {color}; font-size: 0.8em;">[{status_text}]</span>
                    </div>
                </div>
                """
            status_placeholder.markdown(html, unsafe_allow_html=True)
            time.sleep(0.3)
            
    st.session_state.workflow_state = final_state

# --- Main Content ---
st.markdown(f"<h3 style='margin-bottom: 0;'>Sentinel AI — {page}</h3>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: rgba(0, 242, 254, 0.2); margin-top: 0;'>", unsafe_allow_html=True)

if page == "Command Dashboard":
    col1, col2, col3 = st.columns([1, 1.5, 1.5])
    
    with col1:
        st.markdown("<h4 style='color: #00F2FE; font-family: monospace;'>System Execution</h4>", unsafe_allow_html=True)
        if st.button("EXECUTE ANALYSIS PIPELINE", use_container_width=True):
            run_analysis()
            
        st.markdown("<br>", unsafe_allow_html=True)
        if st.session_state.workflow_state:
            state = st.session_state.workflow_state
            
            # Generate static pipeline visual for completed state
            html = ""
            labels = ["Meteorological Sync", "Hydro-gauge Sync", "Citizen Signals", "Historical Records", "Risk Synthesis", "Intervention Plan"]
            for label in labels:
                html += f"<div class='pipeline-step active'><div style='display: flex; justify-content: space-between;'><span>{label}</span><span style='color: #00F2FE; font-size: 0.8em;'>[COMPLETED]</span></div></div>"
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.info("System Idle. Awaiting execution.")
            
    with col2:
        if st.session_state.workflow_state:
            state = st.session_state.workflow_state
            st.markdown("<h4 style='color: #00F2FE; font-family: monospace;'>Real-Time Hydrological Overview</h4>", unsafe_allow_html=True)
            
            # Custom glass metrics
            m1, m2 = st.columns(2)
            with m1:
                rain = state.get('weather_data', {}).get('forecast_mm', 0)
                st.markdown(f"""
                <div class="glass-card">
                    <h4>Precipitation</h4>
                    <p class="glass-value">{rain}<span style="font-size: 1rem; color: #64748B;">mm</span></p>
                    <p class="glass-sub">24h Forecast</p>
                </div>
                """, unsafe_allow_html=True)
            with m2:
                water = state.get('water_data', {}).get('current_level_m', 0)
                danger = state.get('water_data', {}).get('danger_level_m', 8)
                st.markdown(f"""
                <div class="glass-card">
                    <h4>Water Level</h4>
                    <p class="glass-value">{water}<span style="font-size: 1rem; color: #64748B;">/{danger}m</span></p>
                    <p class="glass-sub">{state.get('water_data', {}).get('trend', 'Unknown')}</p>
                </div>
                """, unsafe_allow_html=True)
                
            m3, m4 = st.columns(2)
            with m3:
                reports = state.get('citizen_data', {}).get('complaints_count', 0)
                st.markdown(f"""
                <div class="glass-card">
                    <h4>Citizen Signals</h4>
                    <p class="glass-value">{reports}</p>
                    <p class="glass-sub">Active Telemetry</p>
                </div>
                """, unsafe_allow_html=True)
            with m4:
                risk = state.get("risk_assessment", {})
                score = risk.get('score', 0)
                cat = risk.get('category', 'LOW')
                r_class = "risk-high" if cat == "HIGH" else "risk-medium" if cat == "MEDIUM" else "risk-low"
                st.markdown(f"""
                <div class="glass-card">
                    <h4>Overall Risk</h4>
                    <p class="glass-value {r_class}">{cat}</p>
                    <p class="glass-sub">Index Score: {score}</p>
                </div>
                """, unsafe_allow_html=True)
                
            st.plotly_chart(create_risk_gauge(score), use_container_width=True)

    with col3:
        if st.session_state.workflow_state:
            st.markdown("<h4 style='color: #00F2FE; font-family: monospace;'>Geospatial Risk Map</h4>", unsafe_allow_html=True)
            score = st.session_state.workflow_state.get("risk_assessment", {}).get("score", 0)
            m = create_flood_map(st.session_state.location, score)
            st_folium(m, width=400, height=350)
            
            st.markdown("<br><h4 style='color: #00F2FE; font-family: monospace;'>Autonomous Action Plan</h4>", unsafe_allow_html=True)
            plan = st.session_state.workflow_state.get("action_plan", "")
            if "API Key Missing" in plan:
                st.error(plan)
            else:
                st.markdown(f"<div class='glass-card' style='max-height: 250px; overflow-y: auto; font-size: 0.9em;'>{plan}</div>", unsafe_allow_html=True)

elif page == "Citizen Report":
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<h4 style='color: #00F2FE; font-family: monospace;'>Submit Ground Telemetry</h4>", unsafe_allow_html=True)
        st.write("Route localized observational data into the Sentinel AI intake platform.")
        
        with st.form("report_form"):
            name = st.text_input("Operator Designation (Optional)")
            loc = st.text_input("Coordinates / Location", value=st.session_state.location)
            issue_type = st.selectbox("Anomaly Classification", ["Water Stagnation", "Blocked Drainage", "River Overflow", "Road Flooding"])
            severity = st.select_slider("Severity Index", ["Low", "Medium", "High", "Critical"])
            desc = st.text_area("Event Description")
            
            submitted = st.form_submit_button("TRANSMIT SIGNAL")
            if submitted:
                insert_report(name, loc, issue_type, severity, desc)
                st.success("Telemetry transmitted to Central Matrix.")
                
    with col2:
        st.markdown(f"<h4 style='color: #00F2FE; font-family: monospace;'>Live Feed: {st.session_state.location}</h4>", unsafe_allow_html=True)
        reports = get_reports_by_location(st.session_state.location)
        if reports:
            df = pd.DataFrame(reports, columns=["ID", "Name", "Location", "Issue", "Severity", "Description", "Timestamp"])
            st.dataframe(df.drop(columns=["ID", "Name"]), use_container_width=True)
        else:
            st.info("No active signals in this sector.")

elif page == "Historical Data":
    st.markdown("<h4 style='color: #00F2FE; font-family: monospace;'>Longitudinal Incident Repository</h4>", unsafe_allow_html=True)
    csv_path = os.path.join(os.path.dirname(__file__), "data", "historical_flood_data.csv")
    try:
        df = pd.read_csv(csv_path)
        # Apply some pandas styling if desired, but Streamlit native dataframe is okay
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error("Data matrix offline.")

elif page == "About Project":
    st.markdown("""
    <div class="glass-card">
    <h3 style="color: #00F2FE;">Sentinel AI: Autonomous Flood Defense Architecture</h3>
    <p>Sentinel AI is a distributed, agentic early warning ecosystem that eliminates flood response latency. By continuously synthesizing specialized sub-agents across satellite meteorological feeds, IoT sensor networks, crowdsourced citizen reports, and historical hydrological databases, Sentinel autonomously synthesizes early flood risks and proposes verified mitigation strategies to municipal authorities before floodwaters breach critical thresholds.</p>
    
    <hr style="border-color: rgba(0, 242, 254, 0.2);">
    <h4 style="color: #00F2FE;">Technology Stack</h4>
    <ul>
        <li><b>Orchestration:</b> LangGraph for multi-agent state management.</li>
        <li><b>Intelligence:</b> Google Gemini API for analytical reasoning.</li>
        <li><b>Interface:</b> Streamlit with custom CSS Mission Command UI.</li>
        <li><b>Telemetry:</b> Plotly & Folium for geospatial tracking.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
