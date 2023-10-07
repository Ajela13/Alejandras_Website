# En cargar_datos.py
import csv
from django.core.management.base import BaseCommand
from ViolenciaApp.models import Dane
from datetime import datetime

class Command(BaseCommand):
    help = 'Carga datos desde un archivo CSV a la base de datos'

    def handle(self, *args, **kwargs):
        with open(r'C:\Users\aleja\Downloads\Violence\Reporte_Delito_Violencia_Intrafamiliar_Polic_a_Nacional.csv', encoding='utf-8') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for registro in lector_csv:
                Dane.objects.create(
                    DEPARTAMENTO =registro['DEPARTAMENTO'],
                    MUNICIPIO=registro['MUNICIPIO'],
                    CODIGO_DANE=registro['CODIGO DANE'],
                    ARMAS_MEDIOS=registro['ARMAS MEDIOS'],
                    FECHA_HECHO=(datetime.strptime(registro['FECHA HECHO'],"%d/%m/%Y").date()).strftime("%Y-%m-%d"),
                    GENERO=registro['GENERO'],
                    GRUPO_ETARIO=registro['GRUPO ETARIO'],
                    CANTIDAD=registro['CANTIDAD']
                    )

        self.stdout.write(self.style.SUCCESS('Datos cargados correctamente'))
