import pandas as pd
import folium
import os

m = folium.Map(location=[45.5236, -122.6750])
eq_geo = os.path.join('eq.json')
eq_data = pd.read_csv("eq-range.csv")

m = folium.Map(location=[20.5937,78.9629], zoom_start=4)

folium.Choropleth(
    geo_data=eq_geo,
    name='choropleth',
    data=eq_data,
    columns=['Zone', 'Val'],
    key_on='feature.id',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Risk'
).add_to(m)

folium.LayerControl().add_to(m)

m.save("earthquake.html")
