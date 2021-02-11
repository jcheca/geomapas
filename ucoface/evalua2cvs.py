# -*- coding: UTF-8 -*-
# importing the requests library 
import requests, json
import geopy.distance

  
# api-endpoint 
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

# Cabecera
print "numero;dispositivo;tipo;coor_x;coor_y"

# Extraer dispositivos por tipos
for typename in tipos:

	URL = "http://atd.innolivar.es/orion/v2/entities?type="+typename
	# sending get request and saving the response as response object 
	r = requests.get(url = URL, params = PARAMS, headers = HEADER) 
	# extracting data in json format 
	data = r.json()

	i=0
	while i < len(data):
		if ("location" in data[i]):
			orden+=1
			valores_leg = []
			valores_leg.append(data[i]["location"]["value"]["coordinates"][1])
			valores_leg.append(data[i]["location"]["value"]["coordinates"][0])

			print('{0};{1};{2};{3};{4}'.format(orden,data[i]["id"],data[i]["type"],valores_leg[0],valores_leg[1]))

		i+=1


