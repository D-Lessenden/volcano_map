import folium
import pandas

data = pandas.read_csv("volcano.txt")
lat = list(data["LAT"])
lon = list(data["LON"])


map = folium.Map(location=[38, -99], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

# for coords in [[38, -99], [37, -97]]:
#     fg.add_child(folium.Marker(location=coords, popup="Oh Hello!", icon=folium.Icon(color='green')))

for lt, ln in zip(lat, lon):
     fg.add_child(folium.Marker(location=[lt, ln], popup="Oh Hello!", icon=folium.Icon(color='green')))


map.add_child(fg)

map.save("us_map.html")