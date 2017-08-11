# -*- encoding: utf-8 -*-
import datetime
from app.models import (
    Moneda, Operacion, Usuario)
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', required=False)
    password = serializers.CharField(source='user.password', required=False)
    email = serializers.EmailField(source='user.email', required=False)
    first_name = serializers.CharField(source='user.first_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)
    balance = serializers.DecimalField(max_digits=30, decimal_places=5, required=False, allow_null=True)

    class Meta:
        model = Usuario
        fields = (
            'username', 'password', 'email', 'first_name', 'last_name', 'balance')


class MonedaSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=False)
    simbolo = serializers.CharField(required=False)
    valor_dolar = serializers.DecimalField(max_digits=30, decimal_places=5, required=False, allow_null=True)

    class Meta:
        model = Moneda
        fields = (
            'id', 'nombre', 'simbolo', 'valor_dolar')


class OperacionSerializer(serializers.ModelSerializer):
    importe = serializers.DecimalField(max_digits=30, decimal_places=5, required=False, allow_null=True)
    fecha = serializers.DateTimeField(required=False)
    moneda = serializers.PrimaryKeyRelatedField(read_only=True)
    remitente = serializers.PrimaryKeyRelatedField(read_only=True)
    destinatario = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Operacion
        fields = (
            'id', 'importe', 'fecha', 'moneda', 'remitente', 'destinatario')
