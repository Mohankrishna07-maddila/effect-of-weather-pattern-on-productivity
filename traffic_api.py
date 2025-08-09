# traffic_api.py
import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
TOMTOM_KEY = os.getenv("TOMTOM_API_KEY")

# sample traffic json fallback
SAMPLE_FILE = "sample_traffic.json"

def get_traffic(lat, lon):
    """
    Calls TomTom flowSegmentData endpoint for the point (lat, lon).
    Returns dict: currentSpeed, freeFlowSpeed, currentTravelTime, freeFlowTravelTime, confidence
    If no key or failure, falls back to sample file.
    """
    if TOMTOM_KEY:
        try:
            url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"
            params = {"point": f"{lat},{lon}", "key": TOMTOM_KEY}
            r = requests.get(url, params=params, timeout=15)
            r.raise_for_status()
            js = r.json()
            fs = js.get("flowSegmentData", {})
            return {
                "currentSpeed": fs.get("currentSpeed"),
                "freeFlowSpeed": fs.get("freeFlowSpeed"),
                "currentTravelTime": fs.get("currentTravelTime"),
                "freeFlowTravelTime": fs.get("freeFlowTravelTime"),
                "confidence": fs.get("confidence")
            }
        except Exception as e:
            print("TomTom traffic API error:", e)

    # fallback to sample
    try:
        with open(SAMPLE_FILE, "r", encoding="utf-8") as f:
            js = json.load(f)
            fs = js.get("flowSegmentData", js)
            return {
                "currentSpeed": fs.get("currentSpeed"),
                "freeFlowSpeed": fs.get("freeFlowSpeed"),
                "currentTravelTime": fs.get("currentTravelTime"),
                "freeFlowTravelTime": fs.get("freeFlowTravelTime"),
                "confidence": fs.get("confidence")
            }
    except Exception as e:
        print("Failed to load sample traffic data:", e)
        return None
