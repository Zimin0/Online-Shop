from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import logging

from products.models import Product, Category

logger = logging.getLogger(__name__) # error, warning, critical

def catalog(request):
	""" Главная страница """
	AMOUNT_OF_PRODUCTS = 50
	if request.GET.get('selecter', False) not in ("None", False):
		sort_name = str(request.GET.get('selecter', False))
		products = Product.published.order_by(sort_name)[:AMOUNT_OF_PRODUCTS] # Используется менеджер published. Подробнее написано в моделях.
	else:
		products = Product.published.all()[:AMOUNT_OF_PRODUCTS]
	categories = Category.objects.all().order_by("name")
	context = {
		"products":products,
		"categories":categories,
		}
	return render(request, "catalog/catalog.html", context)

def info(request):
	context = {}
	return render(request, 'catalog/information.html', context)

'''
Аналогичным образом, самый простой способ ограничить доступ к зарегистрированным пользователям в 
ваших представлениях на основе классов - это производные от LoginRequiredMixin. 
Вы должны объявить этот mixin сначала в списке суперкласса, перед классом основного представления.
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin, View):
    ...
Это имеет такое же поведение при переадресации, что и login_required декоратор. 
Вы также можете указать альтернативное местоположение для перенаправления пользователя, если он не
 аутентифицирован (login_url), и имя параметра URL вместо "next" , чтобы вставить текущий абсолютный 
 путь (redirect_field_name).

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    
# Еще одна причина перейти на GET, это то, что GET не должен
# использоваться с методами, которые меняют состояние сервера, 
# а только для read-only операций.

# git add -i
# limit_choices_to={'is_staff': True})

'''