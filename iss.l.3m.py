#!/usr/bin/env python3

import requests
import datetime
import base64

# import requests_cache

# Change path to icon
ICONO = base64.b64encode(open('/home/gabo/sat.png', 'rb').read())
# Catamarca, Argentina
LATITUDE = '-34.6033'
LONGITUDE = '-58.3817'


# Setup cache
# expiration = datetime.timedelta(hours=1)
# requests_cache.install_cache(
#     cache_name='iss_cache', backend='sqlite', expire_after=expiration)


def show(hour, minutes, duration):
    print("[ <span color='#d7ff00'>ISS Próxima Pasada en: </span><span color='#5fffaf'>{}h:{}m</span>"
          " - <span color='#d7ff00'>Duración:</span> <span color='#5fffaf'>{}m</span> ] "
          "| image='{}' imageWidth=20".format(hour, minutes, duration, ICONO.decode()))


def get_pasadas() -> list:
    url = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}'.format(LATITUDE, LONGITUDE)
    response = requests.get(url)
    return response.json()['response']


def get_proxima_pasada() -> tuple:
    pasada = get_pasadas()[0]
    return pasada['risetime'], pasada['duration']


hora_pasada, duracion = get_proxima_pasada()
hora_pasada = datetime.datetime.utcfromtimestamp(hora_pasada)
pasada = hora_pasada - datetime.datetime.utcnow()
segundos_pasada = pasada.seconds
hora = segundos_pasada // 3600
minutos = segundos_pasada % 3600 // 60
duracion = duracion % 3600 // 60

show(hora, minutos, duracion)
