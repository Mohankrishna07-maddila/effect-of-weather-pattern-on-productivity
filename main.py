# main.py
import time
import argparse
from datetime import datetime

from weather_api import get_weather
from traffic_api import get_traffic
from accident_api import get_accidents
from storage import append_row, delete_csv, CSV_FILE

# default location (Hyderabad example). You can change or accept CLI args.
DEFAULT_LAT = 17.3850
DEFAULT_LON = 78.4867

from indian_states import get_random_state

def collect_and_save(lat, lon):
    # fetch sources
    weather = get_weather(lat=lat, lon=lon)
    traffic = get_traffic(lat, lon)
    accidents = get_accidents(lat, lon)

    # Compose row with safe defaults
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temp = weather.get("temp") if weather else None
    humidity = weather.get("humidity") if weather else None
    wind_spd = weather.get("wind_spd") if weather else None
    wdesc = weather.get("description") if weather else None

    current_speed = traffic.get("currentSpeed") if traffic else None
    free_flow = traffic.get("freeFlowSpeed") if traffic else None
    cur_tt = traffic.get("currentTravelTime") if traffic else None
    free_tt = traffic.get("freeFlowTravelTime") if traffic else None
    confidence = traffic.get("confidence") if traffic else None

    acc_count = accidents.get("accident_count") if accidents else 0
    sev = accidents.get("severities") if accidents else {"low":0,"medium":0,"high":0}

    row = [
        timestamp,
        lat, lon,
        temp, humidity, wind_spd, wdesc,
        current_speed, free_flow, cur_tt, free_tt, confidence,
        acc_count, sev.get("low",0), sev.get("medium",0), sev.get("high",0)
    ]

    append_row(row)

def main():
    parser = argparse.ArgumentParser(description="Weather+Traffic+Accident logger")
    parser.add_argument("--lat", type=float, default=DEFAULT_LAT, help="Latitude")
    parser.add_argument("--lon", type=float, default=DEFAULT_LON, help="Longitude")
    parser.add_argument("--interval", type=int, default=300, help="Interval in seconds (default 300 = 5min). Set 0 to run once.")
    parser.add_argument("--delete", action="store_true", help="Delete existing CSV before starting")
    args = parser.parse_args()

    if args.delete:
        delete_csv()

    if args.interval <= 0:
        # run once
        collect_and_save(args.lat, args.lon)
    else:
        print(f"Starting continuous collection every {args.interval} seconds. Press Ctrl+C to stop.")
        entry_count = 0
        cur_state = {"state": "Telangana", "city": "Hyderabad", "lat": args.lat, "lon": args.lon}
        try:
            while True:
                # Change state every 10 entries
                if entry_count % 10 == 0:
                    cur_state = get_random_state()
                    print(f"\nCollecting data for {cur_state['city']}, {cur_state['state']} (lat={cur_state['lat']}, lon={cur_state['lon']})")
                collect_and_save(cur_state['lat'], cur_state['lon'])
                entry_count += 1
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("Stopped by user.")

if __name__ == "__main__":
    main()
