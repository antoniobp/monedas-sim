# -*- encoding: utf-8 -*-
import datetime
from app.models import (
    Moneda, Operacion)
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'username', 'password', 'email', 'first_name', 'last_name')


class MonedaSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=False)
    simbolo = serializers.CharField(required=False)
    valor_dolar = serializers.DecimalField(max_digits=30, decimal_places=5, required=False, allow_null=True)

    class Meta:
        model = Moneda
        fields = (
            'nombre', 'simbolo', 'valor_dolar')


class OperacionSerializer(serializers.ModelSerializer):
    importe = serializers.DecimalField(max_digits=30, decimal_places=5, required=False, allow_null=True)
    fecha = serializers.DateTimeField(required=False)
    moneda = serializers.PrimaryKeyRelatedField(read_only=True)
    remitente = serializers.PrimaryKeyRelatedField(read_only=True)
    destinatario = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Operacion
        fields = (
            'importe', 'fecha', 'moneda', 'remitente', 'destinatario')
