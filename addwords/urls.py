from django.urls import path, include
from .views import main, new_word, ex_word, info, users_list
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
""" Маршрутизатор REST Framework будет следить за тем, чтобы наши запросы динамически попадали в нужный ресурс. 
Если мы добавим или удалим элементы из базы данных, URL-адреса обновятся, чтобы соответствовать."""
router.register(r'words', views.WordViewSet)

#app_name = 'addwords' # чтобы использовать в тегах addwords:название_функции
urlpatterns = [
    path('', main, name='main'),
    path('new/', new_word, name='new'),
    path('<int:word_id>/', ex_word, name='ex_word'), # параметризированный маршрут 
    path('info/', info, name='info'), 
    path('users/', users_list, name='users'),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]