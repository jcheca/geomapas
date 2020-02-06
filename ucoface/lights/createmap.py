# -*- coding: UTF-8 -*-

import glob, os, csv, json
from decimal import Decimal

os.chdir("localidad01")

features = []

for file in glob.glob("*.csv"):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
                latitude = row[2].replace(',','.')
                longitude = row[1].replace(',','.')
                illuminance = float(row[7])
                coordenadas = [float(latitude), float(longitude)]
                properties = {
                   "marker-color": "#7e7e7e",
                   "marker-size": "medium",
                   "marker-symbol": "",
                   "illuminance": illuminance
                }
                geometry = {
                  "type": "Point",
                  "coordinates": coordenadas
                }
                punto = {
                   "type": "Feature",
                   "properties": properties,
                   "geometry": geometry
                }
               
                features.append(punto)

                #print('Processed '+str(line_count)+' lines.')

salida = {
   "type": "FeatureCollection",
   "features": features
}

kk = json.dumps(salida)
print(kk)

