# weather_api.py
import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.getenv("WEATHERBIT_API_KEY")
BASE_URL = "https://api.weatherbit.io/v2.0/current"

# Optional path to sample JSON (used if API key missing or for offline testing)
SAMPLE_FILE = "sample_weather.json"

def get_weather(lat=None, lon=None, city=None, country=None):
    """
    Returns a dict with keys: temp, humidity, wind_spd, description
    If API_KEY missing or request fails, tries to load sample JSON file.
    """
    if API_KEY and ((lat is not None and lon is not None) or city):
        params = {"key": API_KEY}
        if lat is not None and lon is not None:
            params.update({"lat": lat, "lon": lon})
        else:
            params.update({"city": city})
            if country:
                params["country"] = country

        try:
            r = requests.get(BASE_URL, params=params, timeout=15)
            r.raise_for_status()
            js = r.json()
            data = js["data"][0]
            return {
                "temp": data.get("temp"),
                "humidity": data.get("rh"),
                "wind_spd": data.get("wind_spd"),
                "description": data.get("weather", {}).get("description")
            }
        except Exception as e:
            print("Weatherbit API error:", e)

    # fallback to sample file
    try:
        with open(SAMPLE_FILE, "r", encoding="utf-8") as f:
            js = json.load(f)
            data = js["data"][0] if "data" in js and js["data"] else js
            return {
                "temp": data.get("temp"),
                "humidity": data.get("rh"),
                "wind_spd": data.get("wind_spd"),
                "description": data.get("weather", {}).get("description") if "weather" in data else None
            }
    except Exception as e:
        print("Failed to load sample weather data:", e)
        return None
