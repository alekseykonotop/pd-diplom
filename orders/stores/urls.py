from django.urls import path
from .views import PartnerUpdate, PartnerState, PartnerOrders, LoginAccount
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'stores'

urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    # path('api-token-auth/', obtain_auth_token),
]