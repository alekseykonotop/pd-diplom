from django.urls import path
from .views import PartnerUpdate
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'stores'

urlpatterns = [
    path('import-price/', PartnerUpdate.as_view()),
    path('api-token-auth/', obtain_auth_token),
]