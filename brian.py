import pandas as pd
import plotly.express as px

crimes = pd.read_csv('crime_counts.csv', sep=',')
fig = px.histogram(crimes, x='OFFENSE', y='VALUE',nbins=24, width=1000, height=600,title="Count Per Type of Crime")
fig.show()