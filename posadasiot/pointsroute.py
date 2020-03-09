# -*- coding: UTF-8 -*-
# importing the requests library 
import requests, json
import geopy.distance

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

  
# api-endpoint 
URL = "http://atd.innolivar.es/quantum/v2/entities/atdfiware01/value"
HEADER = {
    "Fiware-Service": "smarttrebol",
    "Fiware-ServicePath": "/rabanales"
}
PARAMS = {
    "fromDate": "2020-03-09T06:00:00.000",
    "toDate": "2020-03-09T13:00:00.000"
}

URL1 = "https://reverse.geocoder.ls.hereapi.com/6.2/reversegeocode.json"

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
      localiza = str(data["data"]["attributes"][0]["values"][i])+", "+str(data["data"]["attributes"][1]["values"][i])+",250"
      salida3 = data["data"]["index"][i]
      PARAMS1 = {
          "prox": localiza,
          "mode": "retrieveAddresses",
          "maxresults":"1",
          "gen": "9",
          "apiKey": "...exA4kNikOQqe476JjytZo2hvfJEswXqSB_xx0-3M"
      }

      rr = requests.get(url = URL1, params = PARAMS1)
      data1 = rr.json()
      #krxk = json.dumps(data1, ensure_ascii=False)

      salida1 = ""
      salida2 = ""

      try:
         salida1 = json.dumps(data1["Response"]["View"][0]["Result"][0]["Location"]["Address"]["Street"], ensure_ascii=False)
         #salida1 = data1["Response"]["View"][0]["Result"][0]["Location"]["Address"]["Street"]
      except:
         salida1 = ""

      try:
         salida2 = data1["Response"]["View"][0]["Result"][0]["Location"]["Address"]["HouseNumber"]
      except:
         salida2 = ""
 
      print "{} - {} - {}".format(salida1, salida2, salida3)

      i = i + 1
      localiza = []
