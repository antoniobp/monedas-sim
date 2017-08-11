from django.core.management import BaseCommand
from app.models import Moneda


class Command(BaseCommand):
    help = 'Llena la base con los datos de algunas monedas'

    def handle(self, *args, **options):
        if not Moneda.objects.all():
            peso = Moneda.objects.create(
                nombre='Peso',
                simbolo='AR$',
                valor_dolar=0.05649
            )
            peso.save()

            dolar = Moneda.objects.create(
                nombre='Dólar',
                simbolo='U$D',
                valor_dolar=1
            )
            dolar.save()

            euro = Moneda.objects.create(
                nombre='Euro',
                simbolo='€',
                valor_dolar=1.17695
            )
            euro.save()

            bitcoin = Moneda.objects.create(
                nombre='Bitcoin',
                simbolo='฿',
                valor_dolar=3424.24
            )
            bitcoin.save()
        else:
            print('Monedas ya cargadas')
