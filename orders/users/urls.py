# from django.conf.urls import url
from django.urls import path
from .views import RegisterAccount, ConfirmAccount

app_name = 'users'


urlpatterns = [
    path('register', RegisterAccount.as_view(), name='user-register'),
    path('register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
]