# SENTINEL AI - Agentic Flood Early Warning & Prevention System

## Overview
Sentinel AI is an intelligent multi-agent AI system that detects early flood warning signals from multiple data sources, analyzes the combined risk, and recommends preventive actions before flooding occurs.

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
   streamlit run app.py
   ```
