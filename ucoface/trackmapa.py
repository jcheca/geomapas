# -*- coding: UTF-8 -*-
# importing the requests library 
import requests, json
  
# api-endpoint 
URL = "https://atd.innolivar.es/opendata/cleaner/last50values"

# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 

features = []
 
# Location
for i in range(0,len(data["data"]["attributes"][3]["values"])):

    valores_leg = []
    valores_leg.append(data["data"]["attributes"][3]["values"][i]["longitude"])
    valores_leg.append(data["data"]["attributes"][3]["values"][i]["latitude"])

    properties = {
       "marker-color": "#7e7e7e",
       "marker-size": "medium",
       "marker-symbol": "",
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

# Time
# print(data["data"]["index"])

salida = {
   "type": "FeatureCollection",
   "features": features
}

kk = json.dumps(salida)
print(kk)
