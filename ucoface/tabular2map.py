# -*- coding: UTF-8 -*-

import glob, os, csv, json
from decimal import Decimal

features = []

for file in glob.glob("pepe.txt"):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
                latitude = row[2]
                longitude = row[1]
                illuminance = 0
                coordenadas = [float(latitude), float(longitude)]
                properties = {
                   "marker-color": "#7e7e7e",
                   "marker-size": "medium",
                   "marker-symbol": "",
                   "illuminance": illuminance,
                   "F08140102": row[3],
                   "M08140102": row[4],
                   "F08140304": row[5],
                   "M08140304": row[6],
                   "F08140506": row[7],
                   "M08140506": row[8],
                   "F08140708": row[9],
                   "M08140708": row[10],
                   "F08140910": row[11],
                   
                   "F15180102": row[12],
                   "M15180102": row[13],
                   "F15180304": row[14],
                   "M15180304": row[15],
                   "F15180506": row[16],
                   "M15180506": row[17],
                   "F15180708": row[18],
                   "M15180708": row[19],
                   "F15180910": row[20],
                   "M15180910": row[21],

                   "F19300102": row[22],
                   "M19300102": row[23],
                   "F19300304": row[24],
                   "M19300304": row[25],
                   "F19300506": row[26],
                   "M19300506": row[27],
                   "F19300708": row[28],
                   "M19300708": row[29],
                   "F19300910": row[30],
                   "M19300910": row[31],

                   "F31500102": row[32],
                   "M31500102": row[33],
                   "F31500304": row[34],
                   "M31500304": row[35],
                   "F31500506": row[36],
                   "M31500506": row[37],
                   "F31500708": row[38],
                   "M31500708": row[39],
                   "F31500910": row[40],

                   "F51990102": row[41],
                   "M51990102": row[42],
                   "F51990304": row[43],
                   "M51990304": row[44],
                   "F51990506": row[45],
                   "M51990506": row[46],
                   "F51990708": row[47],
                   "M51990708": row[48],
                   "F51990910": row[49],
                   "M51990910": row[50]
                   
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

