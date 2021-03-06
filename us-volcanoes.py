# Importing the nessassery libraries
import folium
import pandas as pd


### Reading info from Volcano data file
df = pd.read_csv('Volcanoes.txt')


#### Making List from dataframe colomns and zip them to itirate
lat = list(df['LAT'])
lon = list(df['LON'])
name = list(df['NAME'])
elev = list(df['ELEV'])
coordinats = zip(lat, lon, name, elev)


#### Making a object of the folium Map --> Ottawa
map = folium.Map(location=[45.305561, -75.932418],zoom_start=4)


#### Making a FeatureGroup for the Map
fgv = folium.FeatureGroup(name= "Volcanoes")

### Making map colorful by defining the color for each elevation, and call it in forLoop as icon colors
def colors(elev):
    color = ''
    if elev <= 500:
        color = 'red'
    elif elev <= 1000:
        color = 'blue'
    elif elev <= 2000:
        color = 'orange'
    elif elev <= 3000:
        color = 'pink'
    else:
        color = 'green'
    return color

# Itirating through zipped info to make markers on map
for lat, lon, name, elev in coordinats:
    fgv.add_child(folium.Marker(location=[lat, lon], popup= name+' , ' + str(elev), icon=folium.Icon(color=colors(elev)), draggable=False))


### Definding the Feature Group for Population
fgp = folium.FeatureGroup(name='Population')

### Adding country borders
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read()))


#### All FeatureGroups must be added to map as a CHILD
map.add_child(fgv)
map.add_child(fgp)

#### Saving the map to HTML file
map.save("volcanoes.html")