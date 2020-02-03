# -*- coding: UTF-8 -*-

import json
import pymongo

# BBDD
myclient = pymongo.MongoClient("mongodb://localhost:27018")
mydb = myclient["orion-illuminance"]
mycol = mydb["entities"]


with open('salida.geojson') as json_file:
    data = json.load(json_file)
    counter = 1000000

    for p in data['features']:

        longitude = p['geometry']['coordinates'][0]
        latitude = p['geometry']['coordinates'][1]
        illuminance = p['properties']['illuminance']
        coordinates = []
        coordinates.append(latitude)
        coordinates.append(longitude)
        #print(longitude, latitude, illuminance)
        counter += 1

        # MongoDB
        registro = {
           "_id": {
              "id": "POL"+str(counter),
              "type": "Illuminance",
              "servicePath": "/sevilla/mairena"
           },
           "attrNames": ["location", "illuminance"],
           "attrs": {
              "location": {
                 "type": "geo:json",
                 "creDate": 1573072685,
                 "modDate": 1573072685,
                 "value": {
                    "type": "Point",
                    "coordinates": coordinates
                 }
              },
              "illuminance": {
                 "type": "Number",
                 "creDate": 1573072685,
                 "modDate": 1573072685,
                 "value": illuminance,
                 "mdNames": []
              }
           },
           "creDate": 1573072685,
           "modDate": 1573072685,
           "location": {
              "attrName": "location",
              "coords": {
                 "type": "Point",
                 "coordinates": coordinates
              }
           },
           "lastCorrelator": ""

     
        }

        # Grabar registro
        x = mycol.insert_one(registro)

        kk = json.dumps(registro,sort_keys=True)
        print(kk)   


    print (counter)
