import pandas as pd
from geopy.distance import geodesic

# Load crime data
df = pd.read_csv('Crime_Incidents_in_2024.csv')

# Metro stations dictionary (use your full one here — I'll assume you already have this part from your original code)
metro_stations = {
    "Arlington Cemetery": (38.8848, -77.0659),
    "Ballston-MU": (38.8821, -77.1111),
    "Benning Road": (38.8901, -76.9383),
    "Bethesda": (38.9844, -77.0948),
    "Braddock Road": (38.8065, -77.0584),
    "Branch Ave": (38.8264, -76.9125),
    "Brookland-CUA": (38.9332, -76.9948),
    "Capitol Heights": (38.8895, -76.9111),
    "Cheverly": (38.9165, -76.9155),
    "Clarendon": (38.8864, -77.0960),
    "Cleveland Park": (38.9347, -77.0586),
    "College Park-U of Md": (38.9786, -76.9284),
    "Columbia Heights": (38.9287, -77.0325),
    "Congress Heights": (38.8451, -76.9883),
    "Court House": (38.8913, -77.0863),
    "Crystal City": (38.8574, -77.0511),
    "Deanwood": (38.9077, -76.9366),
    "Dunn Loring-Merrifield": (38.8830, -77.2280),
    "Dupont Circle": (38.9096, -77.0431),
    "Eastern Market": (38.8841, -76.9951),
    "Eisenhower Avenue": (38.8004, -77.0715),
    "Farragut North": (38.9033, -77.0391),
    "Farragut West": (38.9014, -77.0395),
    "Federal Center SW": (38.8847, -77.0159),
    "Federal Triangle": (38.8939, -77.0289),
    "Foggy Bottom-GWU": (38.9008, -77.0502),
    "Forest Glen": (39.0154, -77.0423),
    "Fort Totten": (38.9518, -77.0022),
    "Friendship Heights": (38.9604, -77.0841),
    "Gallery Place": (38.8983, -77.0219),
    "Georgia Ave-Petworth": (38.9361, -77.0244),
    "Glenmont": (39.0616, -77.0533),
    "Greenbelt": (39.0110, -76.9113),
    "Greensboro": (38.9200, -77.2361),
    "Grosvenor-Strathmore": (39.0292, -77.1035),
    "Huntington": (38.7937, -77.0752),
    "Judiciary Square": (38.8961, -77.0168),
    "King St-Old Town": (38.8065, -77.0607),
    "Landover": (38.9347, -76.8905),
    "Largo Town Center": (38.9008, -76.8221),
    "McLean": (38.9267, -77.2116),
    "McPherson Square": (38.9013, -77.0338),
    "Medical Center": (38.9990, -77.0970),
    "Minnesota Ave": (38.8983, -76.9483),
    "Morgan Blvd": (38.8913, -76.8680),
    "Mt Vernon Sq 7th St-Convention Center": (38.9047, -77.0222),
    "Navy Yard-Ballpark": (38.8764, -77.0051),
    "Naylor Road": (38.8513, -76.9563),
    "NoMa-Gallaudet U": (38.9072, -77.0022),
    "Pentagon": (38.8695, -77.0533),
    "Pentagon City": (38.8620, -77.0592),
    "Prince George's Plaza": (38.9655, -76.9555),
    "Rhode Island Ave-Brentwood": (38.9209, -76.9951),
    "Rockville": (39.0840, -77.1463),
    "Ronald Reagan Washington National Airport": (38.8534, -77.0440),
    "Rosslyn": (38.8964, -77.0715),
    "Shady Grove": (39.1195, -77.1648),
    "Shaw-Howard U": (38.9127, -77.0223),
    "Silver Spring": (38.9938, -77.0313),
    "Smithsonian": (38.8880, -77.0281),
    "Southern Ave": (38.8411, -76.9754),
    "Spring Hill": (38.9290, -77.2416),
    "Stadium-Armory": (38.8852, -76.9772),
    "Suitland": (38.8493, -76.9321),
    "Takoma": (38.9755, -77.0173),
    "Tenleytown-AU": (38.9478, -77.0783),
    "Twinbrook": (39.0623, -77.1200),
    "Tysons Corner": (38.9200, -77.2231),
    "U Street/African-Amer Civil War Memorial/Cardozo": (38.9165, -77.0288),
    "Union Station": (38.8970, -77.0062),
    "Van Dorn Street": (38.7993, -77.1291),
    "Van Ness-UDC": (38.9436, -77.0639),
    "Vienna/Fairfax-GMU": (38.8778, -77.2724),
    "Virginia Square-GMU": (38.8824, -77.1043),
    "Waterfront": (38.8761, -77.0179),
    "West Falls Church-VT/UVA": (38.9003, -77.1893),
    "West Hyattsville": (38.9541, -76.9698),
    "Wiehle-Reston East": (38.9478, -77.3402),
    "Woodley Park-Zoo/Adams Morgan": (38.9251, -77.0521),
    "Wheaton": (39.0389, -77.0503),
    "White Flint": (39.0481, -77.1135),
    "L'Enfant Plaza": (38.8848, -77.0219),
    "Metro Center": (38.8983, -77.0281)
}

# Function to find closest station
def get_closest_station(lat, lon):
    current_coord = (lat, lon)
    distances = {station: geodesic(current_coord, coords).meters 
                 for station, coords in metro_stations.items()}
    return min(distances, key=distances.get)

# Apply the function to every crime
df['closest_station'] = df.apply(lambda row: get_closest_station(row['LATITUDE'], row['LONGITUDE']), axis=1)

# Filter down to only Columbia Heights crimes
columbia_heights_crimes = df[df['closest_station'] == 'Columbia Heights']

# Parse date and time from REPORT_DAT
columbia_heights_crimes['REPORT_DAT'] = pd.to_datetime(columbia_heights_crimes['REPORT_DAT'])

# Extract day of week and time
columbia_heights_crimes['day_of_week'] = columbia_heights_crimes['REPORT_DAT'].dt.day_name()
columbia_heights_crimes['time'] = columbia_heights_crimes['REPORT_DAT'].dt.strftime('%H:%M:%S')

# Create a smaller dataframe with only what you want
columbia_heights_summary = columbia_heights_crimes[['day_of_week', 'time']]

# Save to CSV
columbia_heights_summary.to_csv('columbia_heights_crimes.csv', index=False)

print("Saved Columbia Heights crimes to 'columbia_heights_crimes.csv'")