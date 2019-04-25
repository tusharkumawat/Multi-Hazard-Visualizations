import folium
import pandas as pd
from folium.plugins import MarkerCluster

# loading data
data = pd.read_csv("Hazards.csv")
lat = data['Latitude']
lon = data['Longitude']
hazardprone = data['Hazard_2011']

# creating base map
map = folium.Map(location=[20.5937,78.9629],tiles='CartoDB dark_matter',zoom_start=5)

# creating cluster
marker_cluster = MarkerCluster().add_to(map)

# color function
def color_change(hazardprone):
    if hazardprone<1000000:
        color='cyan'
    elif 1000000 <= hazardprone < 2000000:
        color='green'
    elif 2000000 <= hazardprone < 3000000:
        color='yellow'
    elif 4000000 <= hazardprone < 4000000:
        color='orange'
    else:
        color='red'
    return color

# adding marker
for lat, lon, hazardprone in zip(lat, lon, hazardprone):
    folium.CircleMarker(location=[lat, lon], radius=9, popup=str(hazardprone)+'m', fill_color=color_change(hazardprone),color='gray',fill_opacity=0.9).add_to(marker_cluster)



# saving map
map.save("map.html")
