import pandas as pd
#find which day had the most crimes in 2024: Tuesday
df = pd.read_csv("Crime_Incidents_in_2024.csv")
df['REPORT_DAT'] = pd.to_datetime(df['REPORT_DAT'], utc=True)
df['Day_name'] = df['REPORT_DAT'].dt.day_name()
day_counts = df["Day_name"].value_counts()

#find which hour of day most crimes occur: 1700
df['HOUR'] = df["REPORT_DAT"].dt.hour
hour_counts = df['HOUR'].value_counts()

#find which crime was most common: THEFT/OTHER
crime_counts = df['OFFENSE'].value_counts()
print(crime_counts)