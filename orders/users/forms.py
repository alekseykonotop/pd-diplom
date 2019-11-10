from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


# class CustomUserCreationForm(UserCreationForm):
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta(UserCreationForm):  # Возможно класс наследования класса Meta надо удалить.
        model = CustomUser
        fields = ('email', 'password1', 'password2', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', )
