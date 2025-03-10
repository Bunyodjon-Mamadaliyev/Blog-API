from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = ['id', 'user', 'bio', 'profile_picture', 'website']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user