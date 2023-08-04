from django.urls import path
from orders.views import new_order

app_name = 'orders'

urlpatterns = [
    path('', new_order, name='new_order'),
]