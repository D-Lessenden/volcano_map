import folium

map = folium.Map(location=[38, -99], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38, -99], popup="Oh Hello!", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("us_map.html")