# -*- coding: UTF-8 -*-
# importing the requests library 
import requests, json
import geopy.distance

  
# api-endpoint 
URL = "https://atdfiware.grayhats.com/orion/v2/entities?type=ztemp"
HEADER = {
    "Fiware-Service": "smarttrebol",
    "Fiware-ServicePath": "/rabanales"
}

# sending get request and saving the response as response object 
r = requests.get(url = URL, headers = HEADER) 
  
# extracting data in json format 
data = r.json() 

#print(data[0])
#exit()

i=0
features=[]
orden=0
while i < len(data):

  try:
     print(data[i]["id"])

     valores_leg = []
     valores_leg.append(data[i]["location"]["value"]["coordinates"][1])
     valores_leg.append(data[i]["location"]["value"]["coordinates"][0])

     properties = {
        "device": data[i]["id"],
        "type": data[i]["type"],
        "update": data[i]["TimeInstant"]["value"]
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
 
  except:
     break

  i+=1

salida = {
   "type": "FeatureCollection",
   "features": features
}

#kk = json.dumps(salida)
#print(kk)

with open('data.json', 'w') as f:
    json.dump(salida, f, ensure_ascii=False, indent=4)