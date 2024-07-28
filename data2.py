import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv('co2_per_capita (1).csv')

# Filter data for the USA
usa_co2_data = data[data['country'] == 'USA']

# Create a line graph for USA CO2 Emissions vs. Year
fig = px.line(
    usa_co2_data, 
    x='year', 
    y='co2_per_capita', 
    title='USA CO2 Emissions Per Capita Over Time',
    labels={'co2_per_capita': 'CO2 Emissions Per Capita (Tonnes)'}
)

fig.update_layout(
    xaxis_title='Year',
    yaxis_title='CO2 Emissions Per Capita (Tonnes)',
    showlegend=False
)

# Save the plot as an interactive HTML file or display it
fig.write_html("usa_co2_plot.html")
