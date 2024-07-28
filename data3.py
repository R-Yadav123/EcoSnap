import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv('cities_air_quality_water_pollution.18-10-2021 (1).csv')

# Clean up column names (they have extra quotes and spaces)
data.columns = data.columns.str.replace('"', '').str.strip()

# Filter for cities in the United States
usa_cities_data = data[data['Country'].str.contains("United States")]

# Create a bar graph comparing Air Quality and Water Pollution indices for each USA city
fig = px.bar(
    usa_cities_data,
    x='City',
    y=['AirQuality', 'WaterPollution'],
    title='Air Quality and Water Pollution Indices in USA Cities',
    labels={'value': 'Index Value', 'variable': 'Index Type'},
    barmode='group'
)

fig.update_layout(
    xaxis_title='City',
    yaxis_title='Index Value',
    xaxis={'categoryorder':'total descending'},
    legend_title='Index Type'
)

# Save the plot as an interactive HTML file or display it
fig.write_html("usa_city_indices.html")