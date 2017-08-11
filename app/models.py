from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    balance = models.DecimalField(max_digits=30, decimal_places=5, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Moneda(models.Model):
    nombre = models.TextField(null=False)
    simbolo = models.TextField(null=False)
    valor_dolar = models.DecimalField(max_digits=30, decimal_places=5, null=False)


class Operacion(models.Model):
    importe = models.DecimalField(max_digits=30, decimal_places=5, null=False)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    moneda = models.ForeignKey('Moneda')
    remitente = models.ForeignKey(Usuario, related_name='%(class)s_operaciones_realizadas')
    destinatario = models.ForeignKey(Usuario, related_name='%(class)s_operaciones_recibidas')

    def as_json(self):
        return dict(
            id=self.id,
            fecha=self.fecha,
            importe=self.importe,
            moneda={
                "nombre": self.moneda.nombre,
                "simbolo": self.moneda.simbolo
            },
            remitente={
                "nombre": self.remitente.user.first_name,
                "apellido": self.remitente.user.last_name,
            },
            destinatario={
                "nombre": self.destinatario.user.first_name,
                "apellido": self.destinatario.user.last_name
            }
        )
