#(L23)curl \
#  -X GET \
#  -H 'Content-Type: *' \
#  --get 'https://route.ls.hereapi.com/routing/7.2/calculateroute.json' \
#    --data-urlencode 'waypoint0=37.8759,-4.7872' \
#    --data-urlencode 'waypoint1=37.8809,-4.7909' \
#    --data-urlencode 'mode=shortest;pedestrian;' \
#    --data-urlencode 'language=es-es' \
#    --data-urlencode 'avoidareas=37.8790,-4.7889;37.8788,-4.7883' \
#    --data-urlencode 'apiKey=exA4kNikOQqe476JjytZo2hvfJEswXqSB_xx0-3M'

#curl \
#  -X GET \
#  -H 'Content-Type: *' \
#  --get 'https://route.ls.hereapi.com/routing/7.2/calculateroute.json' \
#    --data-urlencode 'waypoint0=37.8759,-4.7872' \
#    --data-urlencode 'waypoint1=37.8809,-4.7909' \
#    --data-urlencode 'mode=shortest;pedestrian;' \
#    --data-urlencode 'language=es-es' \
#    --data-urlencode 'avoidareas=37.8790,-4.7889;37.8788,-4.7883!37.8795,-4.7888;37.8794,-4.7885' \
#    --data-urlencode 'apiKey=exA4kNikOQqe476JjytZo2hvfJEswXqSB_xx0-3M'

curl \
  -X GET \
  -H 'Content-Type: *' \
  --get 'https://route.ls.hereapi.com/routing/7.2/calculateroute.json' \
    --data-urlencode 'waypoint0=37.8002,-5.1023' \
    --data-urlencode 'waypoint1=passThrough!37.8035,-5.1055' \
    --data-urlencode 'waypoint2=passThrough!37.8037,-5.1078' \
    --data-urlencode 'waypoint3=passThrough!37.8021,-5.1074' \
    --data-urlencode 'waypoint4=passThrough!37.8012,-5.1086' \
    --data-urlencode 'waypoint5=37.8002,-5.1073' \
    --data-urlencode 'mode=shortest;car;' \
    --data-urlencode 'language=es-es' \
    --data-urlencode 'apiKey=exA4kNikOQqe476JjytZo2hvfJEswXqSB_xx0-3M'
