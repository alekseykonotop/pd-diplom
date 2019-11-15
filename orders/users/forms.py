from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


# class CustomUserCreationForm(UserCreationForm):
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'last_name', 'first_name', 'middle_name',
                  'company', 'position', 'type', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', )
