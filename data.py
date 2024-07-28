import pandas as pd
import plotly.express as px

# Load your data
data = pd.read_csv('global-plastics-production new (2).csv')  # Adjust the filename as necessary

# Create a line graph
fig = px.line(
    data, 
    x='Year', 
    y='Annual plastic production between 1950 and 2019', 
    title='Global Plastic Production Over Time (1950-2019)',
    labels={'Annual plastic production between 1950 and 2019': 'Plastic Production (Tonnes)'}
)

fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Annual Plastic Production (Tonnes)',
    showlegend=False
)

fig.write_html("plot.html")
