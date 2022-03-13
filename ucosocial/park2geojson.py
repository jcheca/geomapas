# -*- coding: UTF-8 -*-
# importing the requests library 
import requests, json
import geopy.distance

  
# api-endpoint 
URL = "https://atdfiware.grayhats.com/orion/v2/entities?limit=1000"
HEADER = {
    "Fiware-Service": "ayto",
    "Fiware-ServicePath": "/cordoba/cordoba"
}

# sending get request and saving the response as response object 
r = requests.get(url = URL, headers = HEADER) 
  
# extracting data in json format 
data = r.json() 

#print(data)
#exit()

i=0
features=[]
orden=0
while i < len(data):

#  try:
#     print(data[i]["location"])
#  except:
#     break

  valores_leg = []
  valores_leg.append(data[i]["location"]["value"]["coordinates"][1])
  valores_leg.append(data[i]["location"]["value"]["coordinates"][0])

  if (int(data[i]["plazas"]["value"]) > 1):
     color_geo = "#ff0000"
  else:
     color_geo = "#0000ff"

  properties = {
     "marker-color": color_geo,
     "marker-size": "small",
     "marker-symbol": "",
     "orden": orden,
     "device": data[i]["id"],
     "type": data[i]["type"],
     "via": data[i]["direccion"]["value"],
     "numero": data[i]["numero"]["value"],
     "barrio": data[i]["barrio"]["value"],
     "distrito": data[i]["distrito"]["value"],
     "plazas": data[i]["plazas"]["value"],
     "rampa": data[i]["rampa"]["value"],
     "disrampa": data[i]["disrampa"]["value"],
     "dimensiones": data[i]["dimensiones"]["value"],
     "estacionamiento": data[i]["estacionamiento"]["value"],
     "leyenda": data[i]["leyenda"]["value"],
     "senial_h": data[i]["senial_h"]["value"],
     "senial_v": data[i]["senial_v"]["value"],
     "sensor_id": data[i]["sensor_id"]["value"],
     "status": data[i]["status"]["value"]

  }

  geometry = {
     "type": "Point",
     "coordinates": valores_leg
  }
  punto = {
     "type": "Feature",
     "properties": properties,
     "geometry": geometry
  }
  features.append(punto)

  i+=1

salida = {
   "type": "FeatureCollection",
   "features": features
}

#kk = json.dumps(salida)
#print(kk)

with open('data.json', 'w') as f:
    json.dump(salida, f, ensure_ascii=False, indent=4)
