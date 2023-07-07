from django.urls import path, include
from .views import main, new_product, ex_product, info, users_list, new_order, ex_category
from rest_framework import routers
from . import views

#router = routers.DefaultRouter()
# """ Маршрутизатор REST Framework будет следить за тем, чтобы наши запросы динамически попадали в нужный ресурс. 
# Если мы добавим или удалим элементы из базы данных, URL-адреса обновятся, чтобы соответствовать."""
#router.register(r'products', views.ProductViewSet)

#app_name = 'addwords' # чтобы использовать в тегах addwords:название_функции
urlpatterns = [
    path('', main, name='main'),
    path('new/', new_product, name='new'),
    path('<int:word_id>/', ex_product, name='ex_product'), # параметризированный маршрут 
    path('info/', info, name='info'), 
    path('users/', users_list, name='users'),
    path('new_order/', new_order, name='new_order'),
    path('<int:category_id>', ex_category, name='ex_category'),
    #path('api/', include('rest_framework.urls', namespace='rest_framework'))
]