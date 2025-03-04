import pandas as pd
df = pd.read_csv("Crime_Incidents_in_2024.csv")
df['REPORT_DAT'] = pd.to_datetime(df['REPORT_DAT'], utc=True)
df['Day_name'] = df['REPORT_DAT'].dt.day_name()
tuesday_data = df[df['Day_name'] == 'Tuesday']
crime_counts = tuesday_data['OFFENSE'].value_counts()

#Breakdown of type of crime that occurs on Tuesday
#THEFT F/AUTO                  1107
#MOTOR VEHICLE THEFT            766
#ROBBERY                        306
#BURGLARY                       162
#ASSAULT W/DANGEROUS WEAPON     154
#SEX ABUSE                       22
#HOMICIDE                        18
#ARSON                            1

df['HOUR'] = df["REPORT_DAT"].dt.hour
time_data = df[df['HOUR'] == 17]
hour_counts = time_data['OFFENSE'].value_counts()

#Breakdown of type of crime that occurs on Tuesday at 1700
#THEFT/OTHER                   823
#THEFT F/AUTO                  591
#MOTOR VEHICLE THEFT           300
#ROBBERY                        84
#BURGLARY                       57
#ASSAULT W/DANGEROUS WEAPON     37
#SEX ABUSE                       6

df = pd.read_csv("Tap&NontapDOTW.csv")

columns_to_clean = ["Avg Daily Tapped Entries", "Avg Daily NonTapped Entries", "Avg Daily Entries"]

for col in columns_to_clean:
    df[col] = df[col].replace({',': ''}, regex=True).astype(int)

df.to_csv("cleaned_tap_DOTW.csv", index=False)