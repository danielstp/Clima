from django.shortcuts import render
from django.http import JsonResponse

def promedio( self, lat, lon, servicios = "noaa,accuweather,weatherdotcom" ):
    suma = 0
    n = 0
    try:
       lat = float(lat)
       lon = float(lon)
    except:
       return JsonResponse({'error':'La longitud y la latitud deben ser nuemros, y pueden tener punto decimal'})
    from promedio.conectores import noaa, accuweather, weatherdotcom
    for servicio in set([x.strip() for x in servicios.split(',')]):
        if( servicio == "accuweather"):
            n = n + 1
            suma = suma + accuweather( lat=lat, lon=lon )
            print(suma)
            print(n)
            continue
        elif( servicio == "noaa" ):
            n = n + 1
            suma = suma + noaa( lat=lat, lon=lon )
            print(suma)
            print(n)
            continue
        elif( "weatherdotcom" ):
            n = n + 1
            suma = suma + weatherdotcom( lat=lat, lon=lon )
            print(suma)
            print(n)
            continue
        else:
            return JsonResponse({'error':'Parametros equivocados'})

    return JsonResponse({'temperaturaPromedio':suma/n})

