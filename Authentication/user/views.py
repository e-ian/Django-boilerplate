import jwt
from Authentication import settings
from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView


class RegisterUser(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]
        email = request.data["email"]

        if not username and not password and not email:
            return Response(
                data={
                    "error": "Missing Information"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )


class LoginUser(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response(
                {
                    'error': 'Please provide both username and password to login'},
                status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {'error': 'Please enter valid credentials'}, status=status.HTTP_404_NOT_FOUND)
        pay_load = {
            'id': user.id,
            'username': user.username
        }
        token = jwt.encode(pay_load, settings.SECRET_KEY)
        print(pay_load)
        return Response({'token': token}, status=status.HTTP_200_OK)
