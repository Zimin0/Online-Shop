from django.urls import path, include
from catalog.views import catalog, info

app_name = 'catalog' # чтобы использовать в тегах catalog:название_функции

urlpatterns = [
    path('', catalog, name='catalog'),
    path('info/', info, name='info'), 
]
