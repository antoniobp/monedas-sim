from django.db import models
from django.contrib.auth.models import User


class Moneda(models.Model):
	nombre = models.TextField(null=False)
	simbolo = models.TextField(null=False)
	valor_dolar = models.TextField(null=False)

class Operacion(models.Model):
	importe = models.DecimalField(max_digits=30, decimal_places=5, null=False)
	fecha = models.DateTimeField(auto_now_add=True, blank=True)
	moneda = models.OneToOneField('Moneda')
	remitente = models.ForeignKey(User, related_name='%(class)s_operaciones_realizadas')
	destinatario = models.ForeignKey(User, related_name='%(class)s_operaciones_recibidas')