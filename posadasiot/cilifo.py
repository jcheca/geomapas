# -*- coding: UTF-8 -*-
# importing the requests library 
from datetime import datetime, timedelta
import requests, json
import geopy.distance

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

  
# api-endpoint 
URL = "http://atd.innolivar.es/quantum/v2/entities/lopy4_02/value"
HEADER = {
    "Fiware-Service": "smarttrebol",
    "Fiware-ServicePath": "/rabanales"
}
PARAMS = {
    "fromDate": "2021-04-22T00:00:00.000",
    "toDate": "2021-04-23T19:00:00.000"
}


# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS, headers = HEADER) 
  
# extracting data in json format 
data = r.json() 

features = []
 
# Location
i = 1
localiza = ""
salida = ""

while i < len(data["data"]["attributes"][0]["values"])-1:

      # datos analizador
      humidity = data["data"]["attributes"][0]["values"][i]
      temperature = data["data"]["attributes"][1]["values"][i]
      velocity = data["data"]["attributes"][2]["values"][i]
      salida3 = data["data"]["index"][i]
 
      print "{},{},{},{},{}".format(i,humidity,temperature,velocity,salida3)

      i = i + 1
      localiza = []
