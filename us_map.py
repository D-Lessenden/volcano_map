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

fg_vol = folium.FeatureGroup(name="Volcanoes")
fg_pop = folium.FeatureGroup(name="Population")

for lt, ln, el in zip(lat, lon, elev):
    fg_vol.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+'m', fill_color=elev_color(el), color = 'grey', fill_opacity=0.7))

fg_pop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 20000000 
else 'orange' if 20000000 <= x['properties']['POP2005'] < 100000000 else 'red'}))


map.add_child(fg_vol)
map.add_child(fg_pop)

map.add_child(folium.LayerControl())

map.save("us_map.html")