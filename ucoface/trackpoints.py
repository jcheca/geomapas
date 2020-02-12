# -*- coding: UTF-8 -*-
# importing the requests library 
import requests, json
import geopy.distance

  
# api-endpoint 
URL = "http://atd.innolivar.es/quantum/v2/entities/rak5205-01/value"
HEADER = {
    "Fiware-Service": "smarttrebol",
    "Fiware-ServicePath": "/rabanales"
}
PARAMS = {
    "fromDate": "2020-02-12T07:00:00.000",
    "toDate": "2020-02-12T13:00:00.000"
}

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS, headers = HEADER) 
  
# extracting data in json format 
data = r.json() 

features = []
 
# Location
base = 0
i = 1
distMax = 5
orden = 0

while i < len(data["data"]["attributes"][3]["values"])-1:

    valores_leg1 = []
    valores_leg2 = []

    valores_leg1.append(data["data"]["attributes"][3]["values"][base]["longitude"])
    valores_leg1.append(data["data"]["attributes"][3]["values"][base]["latitude"])
    valores_leg2.append(data["data"]["attributes"][3]["values"][i]["longitude"])
    valores_leg2.append(data["data"]["attributes"][3]["values"][i]["latitude"])

    lat1 = valores_leg1[0]
    lon1 = valores_leg1[1]
    lat2 = valores_leg2[0]
    lon2 = valores_leg2[1]
   
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)

    distance = geopy.distance.vincenty(coords_1, coords_2).m

    if distance > distMax:    

        if orden == 0:

            # Marcar dos puntos. #1
            #print(distance, base, i)
            properties = {
               "marker-color": "#7e7e7e",
               "marker-size": "small",
               "marker-symbol": "",
               "orden": orden,
               "date": data["data"]["index"][base]
            }
            geometry = {
              "type": "Point",
              "coordinates": valores_leg1
            }
            punto = {
               "type": "Feature",
               "properties": properties,
               "geometry": geometry
            }
            features.append(punto)
            #print(distance, punto)
            #raw_input("Press Enter to continue...")

            # Marcar dos puntos. #2
            properties = {
               "marker-color": "#00ff00",
               "marker-size": "small",
               "marker-symbol": "",
               "orden": orden+1,
               "date": data["data"]["index"][i]
            }
            geometry = {
              "type": "Point",
              "coordinates": valores_leg2
            }
            punto = {
               "type": "Feature",
               "properties": properties,
               "geometry": geometry
            }
            features.append(punto)
            #print(distance, punto)
            #raw_input("Press Enter to continue...")
            orden += 2

        else:

            # Marcar dos puntos. #2
            properties = {
               "marker-color": "#0000ff",
               "marker-size": "small",
               "marker-symbol": "",
               "orden": orden,
               "date": data["data"]["index"][i]
            }
            geometry = {
              "type": "Point",
              "coordinates": valores_leg2
            }
            punto = {
               "type": "Feature",
               "properties": properties,
               "geometry": geometry
            }
            features.append(punto)
            #print(distance, punto)
            #raw_input("Press Enter to continue...")
            orden += 1


        base = i
        i = base+1

    else:
        i += 1

        # Time
        #print(data["data"]["index"])

salida = {
   "type": "FeatureCollection",
   "features": features
}

kk = json.dumps(salida)
print(kk)
