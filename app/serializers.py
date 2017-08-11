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

    def create(self, validated_data):
        """
        Crea el objeto Usuario, asignandole un User de Django
        :param validated_data: los datos que fueron validados en el serializer
        :return: un objeto Usuario con un User asignado
        """
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        usuario = Usuario.objects.create(user=user, **validated_data)
        return usuario

    def update(self, instance, validated_data):
        """
        Modifica un objeto Usuario y un objeto User en caso de que sea necesario
        :param instance: objeto que se quiere actualizar
        :param validated_data: los datos que fueron validados en el serializer
        :return: un objeto Usuario actualizado
        """
        if 'user' in validated_data:
            user_data = validated_data.pop('user')
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.user.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_balance(self, value):
        """
        Valida que el balance sea un número positivo
        :param value:
        :return:
        """
        if value < 0:
            raise serializers.ValidationError("El balance no puede ser negativo")

        return value


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
