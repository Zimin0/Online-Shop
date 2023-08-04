from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# """ Маршрутизатор REST Framework будет следить за тем, чтобы наши запросы динамически попадали в нужный ресурс. 
# Если мы добавим или удалим элементы из базы данных, URL-адреса обновятся, чтобы соответствовать."""
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]