from langgraph.graph import StateGraph, END
from agents.state import FloodSystemState
from agents.weather_agent import weather_node
from agents.water_agent import water_node
from agents.citizen_agent import citizen_node
from agents.historical_agent import historical_node
from agents.risk_agent import risk_node
from agents.action_agent import action_node

def build_workflow():
    """Builds and returns the LangGraph workflow."""
    
    # Initialize the state graph
    workflow = StateGraph(FloodSystemState)

    # Add nodes (Agents)
    workflow.add_node("weather_agent", weather_node)
    workflow.add_node("water_agent", water_node)
    workflow.add_node("citizen_agent", citizen_node)
    workflow.add_node("historical_agent", historical_node)
    workflow.add_node("risk_agent", risk_node)
    workflow.add_node("action_agent", action_node)

    # Define the execution flow
    workflow.set_entry_point("weather_agent")
    
    # Run data-gathering agents sequentially or parallel
    # Here we run them sequentially for simplicity in state updates
    workflow.add_edge("weather_agent", "water_agent")
    workflow.add_edge("water_agent", "citizen_agent")
    workflow.add_edge("citizen_agent", "historical_agent")
    
    # Once all data is gathered, assess risk
    workflow.add_edge("historical_agent", "risk_agent")
    
    # Based on risk, formulate an action plan
    workflow.add_edge("risk_agent", "action_agent")
    
    # End workflow
    workflow.add_edge("action_agent", END)

    # Compile the workflow into a runnable app
    app = workflow.compile()
    return app
