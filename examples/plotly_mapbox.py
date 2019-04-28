#import necessary libraries
import numpy as np 
import pandas as pd
import util
import plotly
import plotly.plotly as py
import plotly.offline as offline
import plotly.graph_objs as go

shaz13_custom_style = "mapbox://styles/shaz13/cjiog1iqa1vkd2soeu5eocy4i"

key = "2009-06-15 17:26:21.0000001"
lon = -73.844311
lat = 40.721319

#set the geo=spatial data
data = [go.Scattermapbox(
            lat=[lat],
            lon=[lon],
            #customdata = (key),
            mode='markers',
            marker=dict(
                size= 4,
                color = 'gold',
                opacity = .1,
            ),
          )]

#set the layout to plot
token = util.getMapboxToken()
layout = go.Layout(autosize=False,
                   mapbox= dict(accesstoken=token,
                                bearing=10,
                                pitch=60,
                                zoom=13,
                                center= dict(lat=40.721319,
                                             lon=-73.987130),
                                style=shaz13_custom_style),
                    width=900,
                    height=600, 
                    title = "Pick up Locations in NewYork")

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig)
