from django.core.management.base import BaseCommand
from fecoval.avaluos.models import Estado, Municipio
import requests


class Command(BaseCommand):
    help = 'Cargar estados y municipios de Mexico'

    def handle(self, *args, **kwargs):
        print('Downloading data...')
        url = "https://github.com/carlosascari/Mexico.json/raw/master/M%C3%A9xico.min.json"
        response = requests.get(url)
        mexico = response.json()
        for estado in mexico:
            estado_obj = Estado()
            estado_obj.clave = estado['clave']
            estado_obj.nombre = estado['nombre']
            estado_obj.save()
            print('Estado', estado['clave'], estado['nombre'])
            for municipio in estado['municipios']:
                municipio_obj = Municipio()
                municipio_obj.clave = municipio['clave']
                municipio_obj.nombre = municipio['nombre']
                municipio_obj.estado = estado_obj
                municipio_obj.save()
        print('Done')
