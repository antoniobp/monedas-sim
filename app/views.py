# -*- encoding: utf-8 -*-
import json
import numbers
import random
import string
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from app.models import Operacion, Moneda
from app.serializers import UserSerializer, OperacionSerializer


@api_view(['POST'])
def auth_login(request):
    """
    Loguea a un usuario en el sistema
    :param request:
    :return:
    """
    data = JSONParser().parse(request)
    try:
        user = authenticate(username=data['username'], password=data['password'])
    except KeyError:
        return Response({"messsage": "Falla en autenticacion"}, status=status.HTTP_400_BAD_REQUEST)

    if user.is_staff:
        return Response({"message": "El usuario admin debe loguearse en /admin"}, status=status.HTTP_400_BAD_REQUEST)

    if user is not None:
        if user.is_active:

            login(request, user)
            return Response({
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "session": request.session.session_key,
                "last_login": str(user.last_login),
                "id": user.id
            }, status=status.HTTP_202_ACCEPTED)
    return Response({"messsage": "No es usuario"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def auth_logout(request):
    """
    Cierra la sesion de un usuario
    :param request:
    :return:
    """
    logout(request)
    return HttpResponse(json.dumps({"messsage": "Logout exitoso"}), content_type="application/json")


@api_view(['GET', 'POST'])
def usuario_lista(request):
    """
    Lista (GET) todos los usuarios o crea (POST) un nuevo usuario
    :param request:
    :return:
    """
    # LISTA TODOS LOS USUARIOS
    if request.method == 'GET':
        try:
            lista_json = []
            lista_users = User.objects.all()

            for user in lista_users:
                if user.is_active and not user.is_staff:
                    user_json = {
                        'username': user.username,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email
                    }
                    lista_json.append(user_json)

            return Response(lista_json)
        except KeyError:
            return Response({"message": "Atributos incorrectos"}, status=status.HTTP_400_BAD_REQUEST)

    # CREA UN USUARIO
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)

            # Verifica que los datos no sean vacios
            if not data:
                return Response({"message": "No se enviaron datos"}, status=status.HTTP_400_BAD_REQUEST)

            # ENCRIPTA EL PASSWORD
            data['password'] = make_password(data['password'])
            serializer = UserSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'username': serializer.data['username'],
                    'first_name': serializer.data['first_name'],
                    'last_name': serializer.data['last_name'],
                    'email': serializer.data['email']
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({"message": "Atributos incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({"message": "Atributos duplicados"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def usuario_datos(request, id_user):
    """
    Obtiene (GET), modifica (PUT) o borra (DELETE) un usuario
    :param request:
    :param id_user: el id del usuario que se quiere obtener, borrar o modificar
    :return:
    """
    if isinstance(id_user, numbers.Number):
        usuario = get_object_or_404(User, pk=id_user)
    else: 
        usuario = get_object_or_404(User, username=id_user)

    # OBTIENE UN USUARIO
    if request.method == 'GET':
        return Response({
            'username': usuario.username,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'email': usuario.last_name
        }

    # ACTUALIZA LOS DATOS DE UN USUARIO VALIDANDO LOS CAMPOS INGRESADOS
    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
            # ENCRIPTA EL PASSWORD
            if 'password' in data:
                data['password'] = make_password(data['password'])

            serializer = UserSerializer(usuario, data=data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    'username': serializer.data['username'],
                    'first_name': serializer.data['first_name'],
                    'last_name': serializer.data['last_name'],
                    'email': serializer.data['email']
                })
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except KeyError:
            return Response({"message": "Atributos incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({"message": "Atributos duplicados"}, status=status.HTTP_400_BAD_REQUEST)

    # BORRA UN USUARIO
    elif request.method == 'DELETE':
        if usuario.validar_delete():
            usuario.user.delete()
            usuario.delete()
            return Response({"messsage": "El usuario ha sido borrado"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"messsage": "No puede borrar"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def operacion_lista(request, id_user):
    """
    Lista (GET) todas las operaciones hechas por un usuario o crea (POST) una nueva
    :param request:
    :param id_user: el id del usuario
    :return:
    """

    usuario = get_object_or_404(User, pk=id_user)

    # VERIFICA QUE EL USUARIO ESTE ACCEDIENDO A SUS DATOS Y NO A LOS DE OTRO
    if not request.user.is_staff:
        if request.user.id != usuario.id:
            return Response({"messsage": "No tiene permisos para acceder"}, status=status.HTTP_401_UNAUTHORIZED)

    # LISTA LAS OPERACIONES DE UN USUARIO
    if request.method == 'GET':

        lista_operaciones = Operacion.objects.filter(remitente=id_user)
        serializers = OperacionSerializer(lista_operaciones, many=True)

    # CREA UN USUARIO
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)

            # Verifica que los datos no sean vacios
            if not data:
                return Response({"message": "No se enviaron datos"}, status=status.HTTP_400_BAD_REQUEST)

            serializer = OperacionSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({"message": "Atributos incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({"message": "Atributos duplicados"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def operacion_datos(request, id_user, id_operacion):
    """
    Obtiene (GET) una operacion
    :param request:
    :param id_user: el id del usuario
    :param id_operacion: el id de la operacion
    :return:
    """

    usuario = get_object_or_404(User, pk=id_user)
    operacion = get_object_or_404(Operacion, pk=id_operacion)

    # VERIFICA QUE EL USUARIO ESTE ACCEDIENDO A SUS DATOS Y NO A LOS DE OTRO
    if not request.user.is_staff:
        if request.user.id != usuario.id:
            return Response({"messsage": "No tiene permisos para acceder"}, status=status.HTTP_401_UNAUTHORIZED)

    # VERIFICA QUE LA OPERACION SE CORRESPONDA CON EL USURIO
    if operacion.remitente != usuario:
        return Response({"messsage": "La operacion no pertenece al usuario"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        "importe": operacion.importe,
        "fecha": operacion.fecha,
        "moneda": operacion.moneda.nombre,
        "remitente": operacion.remitente.first_name + operacion.remitente.last_name,
        "destinatario": operacion.destinatario.first_name + operacion.destinatario.last_name
    })