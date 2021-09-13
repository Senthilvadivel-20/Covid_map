import folium

# initialize the map and store it in a m object
m = folium.Map(location=[42.41394040349264, 20.060817326523722], zoom_start=2.4)


js='countries.geojson'
g=folium.GeoJson(js).add_to(m)
folium.GeoJsonTooltip(fields=['Country','Continent','Population','TotalCases','Recovered','ActiveCases','TotalTests','WHO_Region']).add_to(g)

m.save('map.html')