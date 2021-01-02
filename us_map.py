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
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+'m', fill_color=elev_color(el), color = 'grey', fill_opacity=0.7))
    #    fg.add_child(folium.CircleMarker(location=[lt, ln], raduis = 6, popup=str(el)+'m', fill_color=elev_color(el), color = 'grey', fill_opacity=0.7))


map.add_child(fg)

map.save("us_map.html")