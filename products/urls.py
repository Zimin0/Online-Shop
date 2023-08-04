from django.urls import path
from products.views import new_product, ex_category, ex_product

app_name = 'products'

urlpatterns = [
    path('new/', new_product, name='new'),
    path('<int:product_id>/', ex_product, name='ex_product'), # параметризированный маршрут 
    path('<int:category_id>', ex_category, name='ex_category'),
]