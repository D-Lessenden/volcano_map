import folium
import pandas

data = pandas.read_csv("volcano.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def elev_color(elev):
    if elev < 2000:
        return 'green'
    elif elev > 3000:
        return 'red'
    else:
        return 'orange'


map = folium.Map(location=[38, -99], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+'m', icon=folium.Icon(color=elev_color(el))))
   

map.add_child(fg)

map.save("us_map.html")