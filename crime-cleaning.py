import pandas as pd 
import datetime as dt


df = pd.read_csv('Crime_Incidents_in_2024.csv')

df['REPORT_DAT'] = pd.to_datetime(df['REPORT_DAT'], errors='coerce')
days = df['REPORT_DAT'].dt.weekday.value_counts().sort_values(ascending=False)

print(days)


locations = df['BLOCK'].value_counts().sort_values(ascending=False)
pd.set_option('display.max_rows', None)
filtered_locations = locations[locations > 50]
print(filtered_locations)

# These are most popular blocks for crimes!!
# 3100 - 3299 BLOCK OF 14TH STREET NW            451
# 2000 - 2099 BLOCK OF 8TH STREET NW             200
# 1400 - 1499 BLOCK OF P STREET NW               168
# 812 - 899 BLOCK OF BLADENSBURG ROAD NE         155
# 1737 - 1776 BLOCK OF COLUMBIA ROAD NW          148
# 2300 - 2499 BLOCK OF WASHINGTON PLACE NE       144
# 4227 - 4399 BLOCK OF CONNECTICUT AVENUE NW     142
# 500 - 799 BLOCK OF RHODE ISLAND AVENUE NE      139
# 1000 - 1099 BLOCK OF 16TH STREET NW            128
# 100 - 199 BLOCK OF CARROLL STREET NW           115
# 1516 - 1699 BLOCK OF BENNING ROAD NE           114
# 2600 - 2649 BLOCK OF CONNECTICUT AVENUE NW     113
# 4000 - 4121 BLOCK OF MINNESOTA AVENUE NE       106
# 3200 - 3299 BLOCK OF PENNSYLVANIA AVENUE SE    105
# 600 - 669 BLOCK OF PENNSYLVANIA AVENUE SE      104
# 1100 - 1199 BLOCK OF VERMONT AVENUE NW         104
# 6500 - 6599 BLOCK OF GEORGIA AVENUE NW         102
# 1600 - 1699 BLOCK OF P STREET NW               101
# 3200 - 3275 BLOCK OF M STREET NW               101



































