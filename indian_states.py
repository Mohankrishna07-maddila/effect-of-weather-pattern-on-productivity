# indian_states.py
# List of Indian states with representative city coordinates

import random

INDIAN_STATES = [
    {"state": "Andhra Pradesh", "city": "Vijayawada", "lat": 16.5062, "lon": 80.6480},
    {"state": "Arunachal Pradesh", "city": "Itanagar", "lat": 27.0844, "lon": 93.6053},
    {"state": "Assam", "city": "Guwahati", "lat": 26.1445, "lon": 91.7362},
    {"state": "Bihar", "city": "Patna", "lat": 25.5941, "lon": 85.1376},
    {"state": "Chhattisgarh", "city": "Raipur", "lat": 21.2514, "lon": 81.6296},
    {"state": "Goa", "city": "Panaji", "lat": 15.4909, "lon": 73.8278},
    {"state": "Gujarat", "city": "Ahmedabad", "lat": 23.0225, "lon": 72.5714},
    {"state": "Haryana", "city": "Gurugram", "lat": 28.4595, "lon": 77.0266},
    {"state": "Himachal Pradesh", "city": "Shimla", "lat": 31.1048, "lon": 77.1734},
    {"state": "Jharkhand", "city": "Ranchi", "lat": 23.3441, "lon": 85.3096},
    {"state": "Karnataka", "city": "Bengaluru", "lat": 12.9716, "lon": 77.5946},
    {"state": "Kerala", "city": "Kochi", "lat": 9.9312, "lon": 76.2673},
    {"state": "Madhya Pradesh", "city": "Bhopal", "lat": 23.2599, "lon": 77.4126},
    {"state": "Maharashtra", "city": "Mumbai", "lat": 19.0760, "lon": 72.8777},
    {"state": "Manipur", "city": "Imphal", "lat": 24.8170, "lon": 93.9368},
    {"state": "Meghalaya", "city": "Shillong", "lat": 25.5788, "lon": 91.8933},
    {"state": "Mizoram", "city": "Aizawl", "lat": 23.7271, "lon": 92.7176},
    {"state": "Nagaland", "city": "Kohima", "lat": 25.6701, "lon": 94.1077},
    {"state": "Odisha", "city": "Bhubaneswar", "lat": 20.2961, "lon": 85.8245},
    {"state": "Punjab", "city": "Amritsar", "lat": 31.6340, "lon": 74.8723},
    {"state": "Rajasthan", "city": "Jaipur", "lat": 26.9124, "lon": 75.7873},
    {"state": "Sikkim", "city": "Gangtok", "lat": 27.3314, "lon": 88.6138},
    {"state": "Tamil Nadu", "city": "Chennai", "lat": 13.0827, "lon": 80.2707},
    {"state": "Telangana", "city": "Hyderabad", "lat": 17.3850, "lon": 78.4867},
    {"state": "Tripura", "city": "Agartala", "lat": 23.8315, "lon": 91.2868},
    {"state": "Uttar Pradesh", "city": "Lucknow", "lat": 26.8467, "lon": 80.9462},
    {"state": "Uttarakhand", "city": "Dehradun", "lat": 30.3165, "lon": 78.0322},
    {"state": "West Bengal", "city": "Kolkata", "lat": 22.5726, "lon": 88.3639},
]

def get_random_state():
    return random.choice(INDIAN_STATES)
