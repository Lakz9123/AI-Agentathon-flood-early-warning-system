import folium
import random

def create_flood_map(location="Chennai", risk_score=0):
    """
    Creates a tactical Folium map centered around a location.
    Adds mock data points to visualize risk zones.
    """
    city_coords = {
        "Chennai": [13.0827, 80.2707],
        "Mumbai": [19.0760, 72.8777],
        "Bangalore": [12.9716, 77.5946],
        "Delhi": [28.7041, 77.1025],
        "Pune": [18.5204, 73.8567],
        "Hyderabad": [17.3850, 78.4867]
    }
    
    center = city_coords.get(location, [20.5937, 78.9629])
    
    # Use Dark Matter for tactical look
    m = folium.Map(location=center, zoom_start=12, tiles='CartoDB dark_matter')
    
    num_zones = 8
    for _ in range(num_zones):
        lat = center[0] + random.uniform(-0.08, 0.08)
        lon = center[1] + random.uniform(-0.08, 0.08)
        
        local_risk = risk_score + random.uniform(-20, 20)
        local_risk = max(0, min(100, local_risk))
        
        if local_risk >= 70:
            color = 'red'
            status = 'CRITICAL BREACH'
        elif local_risk >= 40:
            color = 'orange'
            status = 'ELEVATED RISK'
        else:
            color = 'cyan'  # Match neon cyan
            status = 'STABLE'
            
        folium.CircleMarker(
            location=[lat, lon],
            radius=8,
            popup=folium.Popup(f"<div style='font-family: monospace; color: {color};'>STATUS: {status}</div>", max_width=200),
            color=color,
            fill=True,
            fillColor=color,
            fillOpacity=0.7
        ).add_to(m)
        
        # Add connecting lines to simulate network/telemetry routes
        folium.PolyLine(
            locations=[center, [lat, lon]],
            color=color,
            weight=1,
            opacity=0.3,
            dash_array='5, 10'
        ).add_to(m)
        
    return m
