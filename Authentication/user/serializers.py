from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','email')
    def create(self, validated_data):
        password = validated_data.data['password']
        make_password(password)
        return User.objects.create(**validated_data)
