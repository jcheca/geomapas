# -*- coding: UTF-8 -*-
# importing the requests library 
import requests, json
import geopy.distance

  
# api-endpoint 
#URL = "http://atd.innolivar.es/orion/v2/entities?type=Ztemp&attrs=location"
URL = "http://atd.innolivar.es/orion/v2/types"
HEADER = {
    "Fiware-Service": "smarttrebol",
    "Fiware-ServicePath": "/rabanales"
}
PARAMS = {
    "fromDate": "2020-03-03T07:00:00.000",
    "toDate": "2020-03-03T13:00:00.000"
}

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS, headers = HEADER) 
  
# extracting data in json format 
data = r.json() 

features = []
tipos = []
i = 0
orden = 0
 
# Consultar todos los tipos que tenemos 
while i < len(data):
	tipos.append(data[i]["type"])
	i += 1

# Extraer dispositivos por tipos
for typename in tipos:

	URL = "http://atd.innolivar.es/orion/v2/entities?type="+typename
	# sending get request and saving the response as response object 
	r = requests.get(url = URL, params = PARAMS, headers = HEADER) 
	# extracting data in json format 
	data = r.json()

	#print data

	i=0
	while i < len(data):
		try:			
			print data[i]["location"]
			#print data
		except:
			break

		valores_leg = []
		valores_leg.append(data[i]["location"]["value"]["coordinates"][1])
		valores_leg.append(data[i]["location"]["value"]["coordinates"][0])


		properties = {
			"marker-color": "#7e7e7e",
			"marker-size": "small",
			"marker-symbol": "",
			"orden": orden,
			"device": data[i]["id"],
			"type": data[i]["type"]
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


