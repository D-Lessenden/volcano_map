import folium

map = folium.Map(location=[38, -99], zoom_start=6, tiles="Stamen Terrain")
map.save("us_map.html")