from django.urls import path
from .views import main, new_word

#app_name = 'addwords' # чтобы использовать в тегах addwords:название_функции
urlpatterns = [
    path('', main, name='main'),
    path('new/', new_word, name='new' ),
]