# storage.py
import os
import csv
from datetime import datetime

CSV_FILE = "combined_data.csv"
HEADER = [
    "timestamp",
    "lat", "lon",
    # weather
    "temp_c", "humidity_pct", "wind_spd_mps", "weather_desc",
    # traffic
    "current_speed_kmh", "free_flow_speed_kmh", "current_travel_time_s", "free_flow_travel_time_s", "traffic_confidence",
    # accidents
    "accident_count", "accident_low", "accident_medium", "accident_high"
]

def ensure_csv_exists(filename=CSV_FILE):
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)

def append_row(data_row, filename=CSV_FILE):
    ensure_csv_exists(filename)
    with open(filename, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(data_row)
    print(f"Appended row at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} to {filename}")

def delete_csv(filename=CSV_FILE):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted {filename}")
    else:
        print(f"No CSV to delete at {filename}")
