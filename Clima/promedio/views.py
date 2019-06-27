from django.shortcuts import render
from django.http import JsonResponse

def promedio( self, lat, lon, servicios = "noaa,weather,accu" ):
    suma = 0
    n = 0
    from promedio.conectores import noaa, accuweather, weatherdotcom
    for servicio in [x.strip() for x in servicios.split(',')]:
        if( servicio == "accuweather"):
            n = n + 1
            sumaLat = suma + accuweather( lat=lat, lon=lon )
            continue
        elif( servicio == "noaa" ):
            n = n + 1
            suma = suma + noaa( lat=lat, lon=lon )
            continue
        elif( "weatherdotcom" ):
            n = n + 1
            suma = suma + weatherdotcom( lat=lat, lon=lon )
            continue
        else:
            return JsonResponse({'error':'Parametros equivocados'})

    return JsonResponse({'temperaturaPromedio':suma/n})

