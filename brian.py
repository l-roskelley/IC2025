import pandas as pd
import plotly.express as px

crimes = pd.read_csv('crime_counts.csv', sep=',')
px.histogram(crimes, x=crimes['OFFENSE'], y=crimes['VALUE'],nbins=24, width=1000, height=600,title="Count Per Type of Crime")
