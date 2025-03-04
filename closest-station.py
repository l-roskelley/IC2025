import pandas as pd
from geopy.distance import geodesic

# Read CSV file with coordinates
# Assumes your CSV has columns 'latitude' and 'longitude'
df = pd.read_csv('newcsv.csv')

# Dictionary of DC Metro stations and their (latitude, longitude)
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
    # Add additional stations as needed
}

def get_closest_station(lat, lon):
    current_coord = (lat, lon)
    # Calculate the distance from the current coordinate to each station
    distances = {station: geodesic(current_coord, coords).meters 
                 for station, coords in metro_stations.items()}
    # Return the station with the minimum distance
    return min(distances, key=distances.get)

# Apply the function to each row to determine the closest metro station
df['closest_station'] = df.apply(lambda row: get_closest_station(row['LATITUDE'], row['LONGITUDE']), axis=1)

# Print the dataframe with the closest station for each coordinate
# print(df[['LATITUDE', 'LONGITUDE', 'closest_station']])

print(df['closest_station'].value_counts().sort_values(ascending=False))

# results from code


# NoMa-Gallaudet U                                    2200
# Columbia Heights                                    1963
# Rhode Island Ave-Brentwood                          1730
# U Street/African-Amer Civil War Memorial/Cardozo    1678
# Stadium-Armory                                      1622
# Congress Heights                                    1575
# Georgia Ave-Petworth                                1424
# Takoma                                              1071
# Shaw-Howard U                                       1068
# Benning Road                                         955
# Naylor Road                                          930
# Dupont Circle                                        902
# Eastern Market                                       872
# Navy Yard-Ballpark                                   868
# Fort Totten                                          793
# Minnesota Ave                                        781
# Brookland-CUA                                        697
# Foggy Bottom-GWU                                     670
# Mt Vernon Sq 7th St-Convention Center                661
# Deanwood                                             659
# Woodley Park-Zoo/Adams Morgan                        605
# Union Station                                        590
# Tenleytown-AU                                        554
# Metro Center                                         477
# Cleveland Park                                       462
# Farragut North                                       454
# McPherson Square                                     406
# Waterfront                                           317
# Van Ness-UDC                                         305
# Capitol Heights                                      297
# Rosslyn                                              256
# Southern Ave                                         248
# Gallery Place                                        246
# Friendship Heights                                   235
# West Hyattsville                                     140
# Judiciary Square                                     122
# Silver Spring                                        117
# L'Enfant Plaza                                        90
# Federal Center SW                                     88
# Farragut West                                         76
# Federal Triangle                                      38
# Court House                                           30
# Smithsonian                                           20
# Braddock Road                                          1
# Suitland                                               1


#when i removed the grand theft auto crimes and looked at closest stations these are the results
# Columbia Heights                                    1748
# NoMa-Gallaudet U                                    1593
# U Street/African-Amer Civil War Memorial/Cardozo    1489
# Rhode Island Ave-Brentwood                          1412
# Stadium-Armory                                      1286
# Georgia Ave-Petworth                                1204
# Congress Heights                                    1181
# Shaw-Howard U                                        928
# Takoma                                               914
# Dupont Circle                                        851
# Eastern Market                                       741
# Naylor Road                                          708
# Benning Road                                         680
# Navy Yard-Ballpark                                   642
# Foggy Bottom-GWU                                     638
# Fort Totten                                          619
# Minnesota Ave                                        582
# Brookland-CUA                                        555
# Woodley Park-Zoo/Adams Morgan                        544
# Mt Vernon Sq 7th St-Convention Center                541
# Tenleytown-AU                                        531
# Metro Center                                         465
# Union Station                                        465
# Deanwood                                             442
# Farragut North                                       440
# Cleveland Park                                       428
# McPherson Square                                     380
# Van Ness-UDC                                         282
# Waterfront                                           262
# Rosslyn                                              242
# Gallery Place                                        216
# Friendship Heights                                   214
# Capitol Heights                                      187
# Southern Ave                                         183
# Silver Spring                                        106
# Judiciary Square                                     103
# West Hyattsville                                      72
# L'Enfant Plaza                                        72
# Farragut West                                         70
# Federal Center SW                                     69
# Federal Triangle                                      36
# Court House                                           29
# Smithsonian                                           15
# Braddock Road                                          1
# Ronald Reagan Washington National Airport              1