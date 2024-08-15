import csv
from django.core.management.base import BaseCommand
from persona.models import Persona

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
                Persona.objects.create(
                    CEDULA=row[0],
                    CODELEC=row[1],
                    RELLENO=row[2],
                    FECHACADUC=row[3],
                    JUNTA=row[4],
                    NOMBRE=row[5],
                    PRIMER_APELLIDO=row[6],
                    SEGUNDO_APELLIDO=row[7]
                )
        self.stdout.write(self.style.SUCCESS('Datos importados con éxito'))
