import csv
from django.core.management.base import BaseCommand
from persona.models import DisElec

class Command(BaseCommand):
    help = 'Importa personas desde un archivo .txt'

    def add_arguments(self, parser):
        parser.add_argument('archivo', type=str, help='La ruta al archivo .txt con datos separados por comas')

    def handle(self, *args, **kwargs):
        archivo = kwargs['archivo']
        with open(archivo, 'r', encoding='ISO-8859-1') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la cabecera
            for row in reader:
                DisElec.objects.create(
                    CODELE=row[0],
                    PROVINCIA=row[1],
                    CANTON=row[2],
                    DISTRITO=row[3]
                )
        self.stdout.write(self.style.SUCCESS('Datos importados con éxito'))
