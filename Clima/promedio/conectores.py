import requests

def accuweather(lat, lon):

  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
  }

  params = (
    ('latitude', str( lat ) ),
    ('longitude', str( lon ) ),
  )

  response = requests.get('http://localhost:5000/accuweather', headers=headers, params=params)
  a = response.json()

  return aa['simpleforecast']['forecastday'][0]['current']['celsius']

def noaa(lat, lon ):
  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
  }

  params = (
    ('latlon', str( lat ) + ',' + str( lon ) ),
  )

  response = requests.get('http://localhost:5000/noaa', headers=headers, params=params)
  a = response.json()
  return a['today']['current']['celsius']

def weatherdotcom(lat, lon ):
  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
  }

  data = {'lat': str( lat ),'lon': str( lon ) }

  response = requests.post('http://localhost:5000/weatherdotcom', headers=headers, data=data)
  return response