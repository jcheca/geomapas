# -*- coding: UTF-8 -*-

import json
coordinates = []

with open('outpoint.geojson') as json_file:
     data = json.load(json_file)
     data_string = json.dumps(data)
     decoded = json.loads(data_string)
     for leg in decoded["features"]:
         valores_leg = []
         valores_leg.append(leg["geometry"]["coordinates"][0])
         valores_leg.append(leg["geometry"]["coordinates"][1])
         coordinates.append(valores_leg)

     salida = {
        "type": "FeatureCollection",
        "features": [{
           "type": "Feature",
           "properties": {
               "stroke": "#fefb00",
               "stroke-width": 2,
               "stroke-opacity": 1
           },
           "geometry": {
               "type": "LineString",
               "coordinates": coordinates
           }
        }]
     }

     kk = json.dumps(salida)
     print kk
