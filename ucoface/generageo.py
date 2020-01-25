# -*- coding: UTF-8 -*-

import json
from pprint import pprint

with open('salida.json') as json_file:
    data = json.load(json_file)
    data_string = json.dumps(data)
    decoded = json.loads(data_string)
    coordinates = []
    for leg in decoded['response']['route'][0]['leg'][0]['maneuver']:
        valores_leg = []
        valores_leg.append(leg['position']['longitude'])
        valores_leg.append(leg['position']['latitude'])
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
