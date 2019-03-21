from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer

class RegisterUser(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]
        email = request.data["email"]

        if not username  and not password and not email:
            return Response(
                data = {
                    "error": "Missing Information"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer(data = request.data)
        
        # new_user = User.objects.create_user(username=username, password=password, email=email)
        if serializer.is_valid():
            serializer.save()
        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )

        



