# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

# Сериализатор для регистрации пользователя
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


# Сериализатор для логина пользователя
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
            if not user.check_password(data['password']):
                raise AuthenticationFailed('Неверный пароль')
        except User.DoesNotExist:
            raise AuthenticationFailed('Пользователь не найден')
        return data
