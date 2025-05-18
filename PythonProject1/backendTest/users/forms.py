# forms.py
# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # импортируйте вашу модель

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # добавьте другие поля, если нужно


# Форма для логина
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
