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
coordinates = []
 
contador = 0

# Location
for i in range(95,len(data["data"]["attributes"][3]["values"])-1,2):

    # Cada Punto Tomado
    valores_leg_1 = []
    valores_leg_2 = []
    valores_leg_1.append(data["data"]["attributes"][3]["values"][i]["longitude"])
    valores_leg_1.append(data["data"]["attributes"][3]["values"][i]["latitude"])
    valores_leg_2.append(data["data"]["attributes"][3]["values"][i+1]["longitude"])
    valores_leg_2.append(data["data"]["attributes"][3]["values"][i+1]["latitude"])

    # Acumulo puntos
    coordinates.append(valores_leg_1)
    coordinates.append(valores_leg_2)

    # Genera Route
    URL = "https://route.ls.hereapi.com/routing/7.2/calculateroute.json"
    waypoint0 = "geo!"+str(data["data"]["attributes"][3]["values"][i]["latitude"])+","
    waypoint0 = waypoint0+str(data["data"]["attributes"][3]["values"][i]["longitude"])
    waypoint1 = "geo!"+str(data["data"]["attributes"][3]["values"][i+1]["latitude"])+","
    waypoint1 = waypoint1+str(data["data"]["attributes"][3]["values"][i+1]["longitude"])
    mode = "fastest;car;traffic:disabled"
    apiKey = "L23exA4kNikOQqe476JjytZo2hvfJEswXqSB_xx0-3M"
    PARAMS = {
        "waypoint0": waypoint0,
        "waypoint1": waypoint1,
        "mode": mode,
        "apiKey": apiKey
    }

    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    krxk = json.dumps(data)
    print(krxk)
    break


geometry = {
  "type": "LineString",
  "coordinates": coordinates
}
 
objeto = {
   "type": "Feature",
   "geometry": geometry,
   "properties": {}
}
 
features.append(objeto)

               

salida = {
   "type": "FeatureCollection",
   "features":  features
}

kk = json.dumps(salida)
print(kk)
