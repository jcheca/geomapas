# -*- coding: UTF-8 -*-

import glob, os, csv, json
import xlrd

os.chdir("localidad02")

features = []

for file in glob.glob("*.xlsx"):
    with open(file) as csv_file:
        #
        # Apertura/acceso archivo excel. Lectura primera hoja del archivo excel
        #
        book = xlrd.open_workbook(file)
        xl_sheet = book.sheet_by_index(0)

        #
        # Recorrido hojas Excel. Valores Inicialización
        #
        num_cols = xl_sheet.ncols
        line_count = 0
        for row_idx in range(1, xl_sheet.nrows):
            line_count += 1
            # Valor [col:0]
            latitude = xl_sheet.cell_value(row_idx,1)
            longitude = xl_sheet.cell_value(row_idx,0)
            illuminance = xl_sheet.cell_value(row_idx,2)
            coordenadas = [latitude, longitude]
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

        salida = {
           "type": "FeatureCollection",
           "features": features
        }

kk = json.dumps(salida)
print(kk)
