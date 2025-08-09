# accident_api.py
import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
TOMTOM_KEY = os.getenv("TOMTOM_API_KEY")

# bounding box fallback size in degrees (~city area). You can tune it.
DEFAULT_BOX_DELTA = 0.15  # ~15 km box depending on lat
SAMPLE_FILE = "sample_traffic.json"  # sample may include incidents or you can create another sample

def get_accidents(lat, lon, bbox_delta=DEFAULT_BOX_DELTA):
    """
    Returns accident_summary dict:
    { accident_count, severities: {'low': n, 'medium': n, 'high': n}, incidents: [...] }
    Uses TomTom incidentDetails (incidents) endpoint if TOMTOM_KEY present.
    """
    min_lon = lon - bbox_delta
    min_lat = lat - bbox_delta
    max_lon = lon + bbox_delta
    max_lat = lat + bbox_delta
    bbox = f"{min_lon},{min_lat},{max_lon},{max_lat}"

    if TOMTOM_KEY:
        try:
            url = "https://api.tomtom.com/traffic/services/5/incidentDetails"
            params = {"bbox": bbox, "key": TOMTOM_KEY}
            r = requests.get(url, params=params, timeout=15)
            r.raise_for_status()
            js = r.json()
            incidents = js.get("incidents", [])
            # basic severity mapping (depends on returned properties)
            severities = {"low":0, "medium":0, "high":0}
            simple_incidents = []
            for inc in incidents:
                props = inc.get("properties", {})
                # TomTom provides 'impact' or 'severity' in different keys; try several
                sev = props.get("severity") or props.get("impact") or props.get("importance") or props.get("delay")
                # map to simple buckets
                if sev is None:
                    severities["low"] += 1
                    level = "low"
                else:
                    try:
                        val = float(sev)
                        if val <= 1:
                            severities["low"] += 1; level="low"
                        elif val <= 3:
                            severities["medium"] +=1; level="medium"
                        else:
                            severities["high"] +=1; level="high"
                    except:
                        severities["medium"] +=1; level="medium"

                simple_incidents.append({
                    "id": props.get("id") or props.get("externalId") or None,
                    "type": inc.get("type"),
                    "description": props.get("description") or props.get("subType") or "",
                    "severity_level": level
                })

            return {
                "accident_count": len(incidents),
                "severities": severities,
                "incidents": simple_incidents
            }
        except Exception as e:
            print("TomTom incidents API error:", e)

    # fallback to sample file
    try:
        with open(SAMPLE_FILE, "r", encoding="utf-8") as f:
            js = json.load(f)
            incidents = js.get("incidents", [])
            count = len(incidents)
            return {
                "accident_count": count,
                "severities": {"low": count, "medium":0, "high":0},
                "incidents": incidents
            }
    except Exception as e:
        print("Failed to load sample accident data:", e)
        return {"accident_count": 0, "severities": {"low":0,"medium":0,"high":0}, "incidents":[]}
