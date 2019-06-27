from django.shortcuts import render
from django.http import JsonResponse


def promedio(self, lat, lon):
    self.promedio(lat, lon, "noaa", "weather", "accu")

def promedio(self, lat, lon, servicios):
    return JsonResponse({'promedio':5.5})

