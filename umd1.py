#Asher's Code
#If you decide to edit, make sure to push and pull

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

## OUTPUT ##
#OFFENSE
#THEFT/OTHER                   13015
#THEFT F/AUTO                   6680
#MOTOR VEHICLE THEFT            5127
#ROBBERY                        2109
#ASSAULT W/DANGEROUS WEAPON     1026
#BURGLARY                       1004
#HOMICIDE                        187
#SEX ABUSE                       142
#ARSON                             4
#Name: count, dtype: int64