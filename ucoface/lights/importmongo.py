# -*- coding: UTF-8 -*-

import json

with open('salida.geojson') as json_file:
    data = json.load(json_file)
    counter = 1000000

    for p in data['features']:

        longitude = p['geometry']['coordinates'][0]
        latitude = p['geometry']['coordinates'][1]
        illuminance = p['properties']['illuminance']
        coordinates = []
        coordinates.append(longitude)
        coordinates.append(latitude)
        #print(longitude, latitude, illuminance)
        counter += 1

        # MongoDB
        registro = {
           "_id": {
              "id": "POL"+str(counter),
              "type": "Illuminance",
              "servicePath": "/mairena"
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
              },
              "creDate": 1573072685,
              "modDate": 1573072685,
              "lastCorrelator": ""

           }





        }
     
        kk = json.dumps(registro)
        print("---------------")
        print(kk)   
        print("---------------")


    print (counter)
