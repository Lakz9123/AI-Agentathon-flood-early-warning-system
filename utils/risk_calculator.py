def calculate_risk_score(weather_data, water_data, citizen_data, historical_data):
    """
    Calculates a risk score from 0 to 100 based on all input signals.
    """
    score = 0
    reasons = []

    # 1. Weather Factor (0 - 22 points)
    forecast = weather_data.get("forecast_mm", 0)
    if forecast > 100:
        score += 22
        reasons.append(f"Heavy rainfall expected ({forecast} mm).")
    elif forecast > 50:
        score += 12
        reasons.append(f"Moderate rainfall expected ({forecast} mm).")

    # 2. Water Level Factor (0 - 35 points)
    current_level = water_data.get("current_level_m", 0)
    danger_level = water_data.get("danger_level_m", 8.0)
    trend = water_data.get("trend", "Stable")
    
    if current_level >= danger_level:
        score += 35
        reasons.append(f"Water level has reached or exceeded danger mark ({current_level} / {danger_level}m).")
    elif current_level >= danger_level * 0.8:
        score += 25
        reasons.append(f"Water level is approaching danger mark ({current_level} / {danger_level}m).")
    elif current_level >= danger_level * 0.5:
        score += 10
        
    if trend == "Rapidly Rising" or trend == "Rising":
        score += 5
        reasons.append(f"Water level trend is {trend}.")

    # 3. Citizen Signal Factor (0 - 20 points)
    complaints = citizen_data.get("complaints_count", 0)
    if complaints > 10:
        score += 20
        reasons.append(f"High volume of citizen drainage complaints ({complaints}).")
    elif complaints > 3:
        score += 10
        reasons.append(f"Notable increase in citizen complaints ({complaints}).")

    # 4. Historical Risk Factor (0 - 15 points)
    hist_risk = historical_data.get("historical_risk", "Low")
    if hist_risk == "High":
        score += 15
        reasons.append("Location has a high historical flood risk.")
    elif hist_risk == "Medium":
        score += 5
        reasons.append("Location has a medium historical flood risk.")

    # Cap score at 100
    score = min(100, score)

    # Determine risk category
    if score >= 70:
        category = "HIGH"
    elif score >= 40:
        category = "MEDIUM"
    else:
        category = "LOW"

    return {
        "score": score,
        "category": category,
        "reasons": reasons
    }
