import plotly.graph_objects as go
import pandas as pd

# Sample data
data = {
    'City': ['Budapest', 'Debrecen', 'Szeged'],
    'Lat': [47.4979, 47.5316, 46.2530],
    'Lon': [19.0402, 21.6273, 20.1414],
    'Value': [100, 80, 60]  # Sample values for each city
}

df = pd.DataFrame(data)

# Create map figure
fig = go.Figure(go.Scattermapbox(
    mode='markers+text',
    lat=df['Lat'],
    lon=df['Lon'],
    marker=go.scattermapbox.Marker(size=df['Value']),
    text=df['City'],
))

# Update layout
fig.update_layout(
    mapbox=dict(
        style='open-street-map',
        zoom=4,
        center=dict(lat=47.5, lon=19)
    ),
    margin=dict(r=0, l=0, t=0, b=0),
)

# Show the plot
fig.show()
