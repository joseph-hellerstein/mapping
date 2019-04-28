import folium
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

FILE = "Seattle_Real_Time_Fire_911_Calls.csv" 
SEATTLE_COORDINATES = (47.6062, -122.3321)
data = pd.read_csv(FILE)
 
# for speed purposes
MAX_RECORDS = 10
  
# create empty map zoomed in on San Francisco
map = folium.Map(location=SEATTLE_COORDINATES, zoom_start=12)
 
# add a marker for every record in the filtered data, use a clustered view
for _, row in data[0:MAX_RECORDS].iterrows():
  popup=folium.Popup(row['Address'], max_width=450)
  folium.Marker([row['Latitude'], row['Longitude']], popup=popup).add_to(map)
map.save("map.html")

# Dashify

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1("Seattle map"),
    html.Iframe(id='map', srcDoc=open("map.html", "r").read(),
        width="100%", height="600")
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
