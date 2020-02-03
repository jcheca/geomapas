# Query 5 mts from point (longitud, latitud)
curl --location --request GET 'http://localhost:1026/v2/entities?georel=near;maxDistance:5&geometry=point&coords=-6.036955,37.352515' \
--header 'Fiware-Service: illuminance' \
--header 'Fiware-ServicePath: /sevilla/mairena'

# Get ALL Entities
#curl --location --request GET 'http://localhost:1026/v2/entities' \
#--header 'Fiware-Service: illuminance' \
#--header 'Fiware-ServicePath: /sevilla/mairena'

# Get ONE Entities
#curl --location --request GET 'http://localhost:1026/v2/entities/POL1006576' \
#--header 'Fiware-Service: illuminance' \
#--header 'Fiware-ServicePath: /sevilla/mairena'
