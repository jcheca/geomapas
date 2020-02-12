# -*- coding: UTF-8 -*-

import json, requests

URL = "https://route.ls.hereapi.com/routing/7.2/calculateroute.json"
PARAMS = {
    "mode": "fastest;car;traffic:disabled",
    "apiKey": "L23exA4kNikOQqe476JjytZo2hvfJEswXqSB_xx0-3M"
}
count = 0
with open('outline.geojson') as json_file:
     data = json.load(json_file)
     data_string = json.dumps(data)
     decoded = json.loads(data_string)
     maxList = len(decoded["features"][0]["geometry"]["coordinates"])
     for leg in decoded["features"][0]["geometry"]["coordinates"]:
         if count == 0 or count == maxList-1:
            PARAMS.update({"waypoint"+str(count): str(leg[1])+","+str(leg[0])})         
         else:
            PARAMS.update({"waypoint"+str(count): "passThrough!"+str(leg[1])+","+str(leg[0])})         
         count += 1
     #print(PARAMS)

     r = requests.get(url = URL, params = PARAMS)
     data = r.json()
     krxk = json.dumps(data)
     print(krxk)
