from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.response import Response

class RegisterUser(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")

        if not username  and not password and not email:
            return Response(
                data = {
                    "error": "Missing Information"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(username=username, password=password, email=email)
        return Response(
            data={
                "Username": username,
                "Password": password,
                "email": email
            },
            status=status.HTTP_201_CREATED

        )

        



