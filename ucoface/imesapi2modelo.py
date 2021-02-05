# -*- coding: UTF-8 -*-

import glob, os, csv, json
import xlrd
import re
import random

line_count = 0

aSex = "F "
aOld = 20
aVis = 0.8

combina = ["F08140102","M08140102",
           "F08140304","M08140304",
           "F08140506","M08140506",
           "F08140708","M08140708",
           "F08140910","M08140910",

           "F15180102","M15180102",
           "F15180304","M15180304",
           "F15180506","M15180506",
           "F15180708","M15180708",
           "F15180910","M15180910",

           "F19300102","M19300102",
           "F19300304","M19300304",
           "F19300506","M19300506",
           "F19300708","M19300708",
           "F19300910","M19300910",

           "F31500102","M31500102",
           "F31500304","M31500304",
           "F31500506","M31500506",
           "F31500708","M31500708",
           "F31500910","M31500910",

           "F51990102","M51990102",
           "F51990304","M51990304",
           "F51990506","M51990506",
           "F51990708","M51990708",
           "F51990910","M51990910"

]

def dms2dd(s):
    degrees, minutes, seconds, direction = re.split(' ', s)
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction in ('S','W'):
        dd*= -1
    return dd

#
# Genera cabecera
#
print "Numero;NombreCalle;SexoPO;EdadPO;CoordXPO;CoordYPO;LUXPO;LUXPA;DistLECT;AGUDEZAVISUAL"

#
# Main
#
for file in glob.glob("*.xlsx"):
    with open(file) as csv_file:
        #
        # Apertura/acceso archivo excel. 
        #
        book = xlrd.open_workbook(file)
        nsheet = len(book.sheet_names())

        #
        # Para cada combinacion
        #
        for task in combina:

            line_count = 0
            aSex = task[0:1]
            aOld_ini = int(task[1:3])
            aOld_fin = int(task[3:5])
            aVis_ini = int(task[5:7])
            aVis_fin = int(task[7:9])
 
            #
            # Para todas las hojas del archivo .xlsx
            #
            for num_sheet in range(0, nsheet):
                xl_sheet = book.sheet_by_index(num_sheet)

                #
                # Recorrido hojas Excel. Valores Inicialización
                #
                num_cols = xl_sheet.ncols

                for row_idx in range(1, xl_sheet.nrows):

                    # DEBUG only
                    #if row_idx == 1:
                    #   print xl_sheet.cell_value(row_idx,1)
                    #   raw_input("Pulsa una tecla")


                    line_count += 1
                    # Valor [col:0]
                    latitude = xl_sheet.cell_value(row_idx,5).strip()
                    n_latitd = dms2dd(latitude)
                    longitude = xl_sheet.cell_value(row_idx,6).strip()
                    n_longitd = dms2dd(longitude)
                    lux = xl_sheet.cell_value(row_idx,4).strip()[4:]
                    # random aOld
                    aOld = random.randint(aOld_ini, aOld_fin)
                    aVis = (random.randint(aVis_ini, aVis_fin)*1.0)/10

                    print('{0};{1};{2};{3};{4};{5};{6};{7};;{8}'.format(line_count,task,aSex,aOld,n_latitd,n_longitd,lux.strip(),lux.strip(),aVis))

