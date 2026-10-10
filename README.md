# SENTINEL AI - Agentic Flood Early Warning & Prevention System

## Overview
Sentinel AI is an intelligent multi-agent AI system that detects early flood warning signals from multiple data sources, analyzes the combined risk, and recommends preventive actions before flooding occurs.

## Architecture
The backend is built with **FastAPI** and uses a **LangGraph** flow orchestrated through 6 specialized agents:
1. **Weather Agent**: Gathers and processes meteorological data.
2. **Water Agent**: Monitors hydro-gauge telemetry.
3. **Citizen Agent**: Analyzes crowdsourced incident reports.
4. **Historical Agent**: Cross-references with past flood event databases.
5. **Risk Agent**: Synthesizes inputs into an overall risk score.
6. **Action Agent (Gemini)**: Reasons over the state to generate a targeted prevention plan.

The pipeline flow is: `weather -> water -> citizen -> historical -> risk -> action`

## Setup Instructions

1. Clone or copy the repository.
2. Ensure you have Python installed.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and configure your API keys:
   ```bash
   cp .env.example .env
   ```
   Provide your `GEMINI_API_KEY`.
5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
6. Access the dashboard at `http://localhost:8000`.

## Demo Mode
In demo mode, simulated data sets are loaded for predetermined regions (e.g., Chennai, District 4) to demonstrate system logic without relying on live external sensors. You can trigger this mode in the web UI.
