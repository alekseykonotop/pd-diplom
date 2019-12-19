from django.urls import path
from .views import PartnerUpdate, PartnerState, PartnerOrders
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'stores'

urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    # path('api-token-auth/', obtain_auth_token),
]