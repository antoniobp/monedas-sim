from django.test import TestCase
from app.models import Usuario, Operacion
from app.serializers import UserSerializer, OperacionSerializer


class UsuarioTests(TestCase):
    def test_balance_positivo(self):
        usuario = Usuario()

        data = {
            "username": "pepe",
            "first_name": "jose",
            "last_name": "perez",
            "password": "1234",
            "email": "pepe@pepe.com",
            "balance": 1000
        }

        serializer = UserSerializer(usuario, data=data)

        self.assertEqual(serializer.is_valid(), True)

    def test_balance_negativo(self):
        usuario = Usuario()

        data = {
            "username": "pepe",
            "first_name": "jose",
            "last_name": "perez",
            "password": "1234",
            "email": "pepe@pepe.com",
            "balance": -10
        }

        serializer = UserSerializer(usuario, data=data)

        self.assertEqual(serializer.is_valid(), False)

    def test_balance_cero(self):
        usuario = Usuario()

        data = {
            "username": "pepe",
            "first_name": "jose",
            "last_name": "perez",
            "password": "1234",
            "email": "pepe@pepe.com",
            "balance": 0
        }

        serializer = UserSerializer(usuario, data=data)

        self.assertEqual(serializer.is_valid(), False)


class OperacionTests(TestCase):
    def test_importe_positivo(self):
        operacion = Operacion()

        data = {
            "importe": 1000
        }

        serializer = OperacionSerializer(operacion, data=data)

        self.assertEqual(serializer.is_valid(), True)

    def test_importe_negativo(self):
        operacion = Operacion()

        data = {
            "importe": -10
        }

        serializer = OperacionSerializer(operacion, data=data)

        self.assertEqual(serializer.is_valid(), False)

    def test_importe_cero(self):
        operacion = Operacion()

        data = {
            "importe": 0
        }

        serializer = OperacionSerializer(operacion, data=data)

        self.assertEqual(serializer.is_valid(), False)

    def test_remitente_destinatario_iguales(self):
        operacion = Operacion()

        data = {
            "importe": 10
        }

        serializer = OperacionSerializer(operacion, data=data)

        self.assertEqual(serializer.is_valid(), False)