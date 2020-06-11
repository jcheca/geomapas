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
URL = "http://atd.innolivar.es/quantum/v2/entities/atdfiware01/value"
HEADER = {
    "Fiware-Service": "smarttrebol",
    "Fiware-ServicePath": "/rabanales"
}
PARAMS = {
    "fromDate": "2020-06-11T03:00:00.000",
    "toDate": "2020-06-11T14:00:00.000"
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

      # datos analizador
      battery_level = data["data"]["attributes"][0]["values"][i]
      dl_counter = data["data"]["attributes"][1]["values"][i]
      gps_quality = data["data"]["attributes"][2]["values"][i]
      hdop = data["data"]["attributes"][3]["values"][i]
      lati_hemisphere = data["data"]["attributes"][4]["values"][i]
      latitude = data["data"]["attributes"][5]["values"][i]
      lattitude_dm = data["data"]["attributes"][6]["values"][i]
      long_hemisphere = data["data"]["attributes"][7]["values"][i]
      longitude = data["data"]["attributes"][8]["values"][i]
      longitude_dm = data["data"]["attributes"][9]["values"][i]
      rssi_dl = data["data"]["attributes"][11]["values"][i]
      sats = data["data"]["attributes"][12]["values"][i]
      snr_dl = data["data"]["attributes"][13]["values"][i]
      temperature = data["data"]["attributes"][14]["values"][i]
      ul_counter = data["data"]["attributes"][15]["values"][i]
      localiza = str(data["data"]["attributes"][5]["values"][i])+", "+str(data["data"]["attributes"][8]["values"][i])+",250"

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
      except:
         salida1 = ""

      try:
         salida2 = data1["Response"]["View"][0]["Result"][0]["Location"]["Address"]["HouseNumber"]
      except:
         salida2 = ""
 
      print "{},{},{},{},{},{},{},{},{},{},{},{},{}".format(battery_level,gps_quality,lati_hemisphere,latitude,long_hemisphere,longitude,rssi_dl,sats,snr_dl, temperature, salida1, salida2, salida3)

      i = i + 1
      localiza = []
