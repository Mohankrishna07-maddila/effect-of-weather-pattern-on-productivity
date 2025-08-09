def analyze_safety(weather):
    temp = weather["temp"]
    condition = weather["condition"].lower()

    if "storm" in condition or "thunder" in condition:
        return "⚠️ Dangerous weather — avoid traveling."
    elif "rain" in condition:
        return "☔ Rainy weather — travel with caution."
    elif temp < 5:
        return "❄ Cold weather — wear warm clothes."
    elif temp > 35:
        return "🔥 Hot weather — stay hydrated."
    else:
        return "✅ Safe weather for travel."
