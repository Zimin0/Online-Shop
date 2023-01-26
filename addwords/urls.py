from django.urls import path
from .views import main, new_word


urlpatterns = [
    path('main/', main, name='main'),
    path('new/', new_word, name='new' )
]