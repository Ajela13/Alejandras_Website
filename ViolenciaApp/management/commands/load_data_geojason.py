# En cargar_datos.py
import json
from urllib.request import urlopen
from django.core.management.base import BaseCommand
from ViolenciaApp.models import Geojason

class Command(BaseCommand):
    help = 'Carga datos desde un archivo JSON a la base de datos'

    def handle(self, *args, **kwargs):
        with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as archivo_json:
            colombia_data = json.load(archivo_json)
            geoJson = Geojason.objects.create(
                type=colombia_data['type'],
                crs=colombia_data['crs'],
                features=colombia_data['features'],
            )

            geoJson
        self.stdout.write(self.style.SUCCESS('Datos cargados correctamente'))
