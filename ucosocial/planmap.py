# -*- coding: UTF-8 -*-
# Reading an excel file using Python
import pandas as pd
import json

#pd.set_option('max_columns', None)

df1 = pd.read_excel('trabajo.xlsx',sheet_name='Plazas PMR')
#df1['Columna5'] = df1['Columna5'].fillna("")
#df1['Columna6'] = df1['Columna6'].fillna("")
df1 = df1.fillna("")

# Columnas
# 01: Numero
# 02: Via
# 03: Numero Postal
# 04: Geocoordenadas
# 05: Distrito
# 06: Barrio
# 07: Numero de Plazas
# 08: Estacionamiento
# 09: Dimensiones (m)
# 10: Rampa (ppr)
# 11: Distancia a rampa o PPR (m)
# 12: Señalización vertical
# 13: Leyenda
# 14: Señalización Horizontal

# Funcion Referencia
def referencia(ref_a,ref_b):
    return str(ref_a)[-3:]+str(ref_b)[-3:]


def textlatlon(entrada):
    # GRADOS
    grados = entrada.strip().split("°")

    # MINUTOS (dos caracteres distintos delimitado)
    if (grados[1].strip().find("'") != -1):
       minuto = grados[1].strip().split("'")
    else:
       if (grados[1].strip().find("′") != -1):
          minuto = grados[1].strip().split("′")

    # SEGUNDOS (dos caracteres distintos delimitado)
    if (grados[1].strip().find('"') != -1):
       segundos = minuto[1].strip().split('"')
    else:
       if (grados[1].strip().find('″') != -1):
          segundos = minuto[1].strip().split('″')

    segundos[0] = segundos[0].replace(",", ".")

    dd = float(grados[0]) + float(minuto[0])/60 + float(segundos[0])/(60*60);
    if segundos[1] in ('S','O'):
        dd*= -1

    return dd

def disallowed(entrada):
    disallowed_characters = '()<>;="'+"'"
    for character in disallowed_characters:
       entrada = entrada.replace(character, "")
    return entrada


# MAIN
for i in df1.index:

    # Division "latitud"
    if (df1['Columna4'][i].strip().find(";") != -1):
       resultado = df1['Columna4'][i].strip().split(";")
    else:
       if (df1['Columna4'][i].strip().find("-") != -1):
          resultado = df1['Columna4'][i].strip().split("-")

    # Depuración
    # print(df1['Columna1'][i],df1['Columna4'][i].strip(),textlatlon(resultado[0]),",",textlatlon(resultado[1]))

    lat = textlatlon(resultado[0])
    long = textlatlon(resultado[1])
    location = [lat, long]

    orden = df1['Columna1'][i]
    nplaz = df1['Columna7'][i]

    for objeto in range(nplaz):
        nref_a = 1000 + orden
        nref_b = 1001 + objeto

        payload = {
                     "id": "urn:ngsi-ld:ipark:odb"+referencia(nref_a,nref_b),
                     "type": "ipark",
                     "direccion": {
                         "type": "String",
                         "value": disallowed(df1['Columna2'][i])
                     },
                     "numero": {
                         "type": "String",
                         "value": df1['Columna3'][i]
                     },
                     "location": {
                         "type": "geo:json",
                         "value": {
                            "type": "Point",
                            "coordinates": location
                         }
                     },
                     "distrito": {
                         "type": "String",
                         "value": disallowed(df1['Columna5'][i])
                     },
                     "barrio": {
                         "type": "String",
                         "value": disallowed(df1['Columna6'][i])
                     },
                     "plazas": {
                        "type": "String",
                        "value": str(df1['Columna7'][i])
                     },
                     "estacionamiento": {
                        "type": "String",
                        "value": df1['Columna8'][i]
                     },
                     "dimensiones": {
                        "type": "String",
                        "value": df1['Columna9'][i]
                     },
                     "rampa": {
                        "type": "String",
                        "value": df1['Columna10'][i]
                     },
                     "disrampa": {
                        "type": "String",
                        "value": disallowed(df1['Columna11'][i])
                     },
                     "senial_v": {
                        "type": "String",
                        "value": df1['Columna12'][i]
                     },
                     "leyenda": {
                        "type": "String",
                        "value": df1['Columna13'][i]
                     },
                     "senial_h": {
                        "type": "String",
                        "value": df1['Columna14'][i]
                     },
                     "status": {
                        "type": "String",
                        "value": ""
                     },
                     "sensor_id": {
                        "type": "String",
                        "value": ""
                     }
        


                  }

        print('echo "'+str(i+1)+'"')
        varpost = "curl localhost:1026/v2/entities/ -s -S --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'fiware-service: ayto' --header 'fiware-servicepath: /cordoba/cordoba' -d @- <<EOF"
        print(varpost)
        print(json.dumps(payload,indent=4,ensure_ascii=False))
        print("EOF")
        print("sleep 2")
