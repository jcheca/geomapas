# -*- coding: UTF-8 -*-

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

#
# Noº de puntos a procesar y definición de matrix
#
numlec = 45872
matrix = x = [[0 for i in range(54)] for j in range(numlec+1)]

# Using readlines()
file1 = open('out-modelo.csv', 'r')
Lines = file1.readlines()

# Strips the newline character
for line in Lines:

    # read lines. divide bay ";" char
    a = line.strip()
    b = a.split(";")
 
    # set de variables 
    num_id = int(b[0].replace('"', ''))
    cmb_id = b[1].replace('"', '').strip()
    cor_xx = b[2].replace('"', '').strip()
    cor_yy = b[3].replace('"', '').strip()
    drf_nn = b[5].replace('"', '').strip()
    lux_pt = b[7].replace('"', '').strip()

    # for DEBUG 
    #print('{0};{1};{2};{3};{4}'.format(num_id,cmb_id,cor_xx,cor_yy,drf_nn))
    
    # fill matrix
    matrix[num_id][0] = num_id
    matrix[num_id][1] = cor_xx
    matrix[num_id][2] = cor_yy
    matrix[num_id][3] = lux_pt
    matrix[num_id][combina.index(cmb_id)+4] = drf_nn

    #raw_input("Pulse una tecla ...")
 
# Build header (line 0)
campos = ''
for combinaciones in combina:
    campos = campos + combinaciones+";"
print "registro;coor_x;coor_y;lux;"+campos

# print info to export
for row_idx in range(1, numlec+1):
    for linea in range(0,53):
        print('{0};'.format(matrix[row_idx][linea])),
    print('{0}'.format(matrix[54][linea]))

