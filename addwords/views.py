from django.shortcuts import render, redirect, HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User



# Еще одна причина перейти на GET, это то, что GET не должен
# использоваться с методами, которые меняют состояние сервера, 
# а только для read-only операций.

def main(request):
	AMOUNT_OF_PRODUCTS = 15
	if request.GET.get('selecter', False) not in ("None", False):
		sort_name = str(request.GET.get('selecter', False))
		products = Product.objects.filter(archived=False).order_by(sort_name)[:AMOUNT_OF_PRODUCTS] 
	else:
		products = Product.objects.filter(archived=False)[:AMOUNT_OF_PRODUCTS]
	context = {"products":products}

	return render(request, "addwords/main.html", context)

#@login_required # будет перебрасывать на страницу LOGIN_URL, если юзер не вошел в систему.
# Вы можете сделать то же самое вручную, путём тестирования request.user.is_authenticated, но декоратор намного удобнее!
def new_product(request):
	"""Добавление товара заказа."""
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES) # request.FILES - для загрузки файлов
		if form.is_valid():
			product = form.save(commit=False)
			product.saller = request.user # request.user возвращает текущего пользователя
			product.save()
			return redirect('main')
	else:
		form = ProductForm()
	return render(request, 'addwords/newOrder.html', {'form': form}) 

def new_order(request):
	"""Добавление нового заказа."""
	if request.method == 'POST':
		form = OrderForm(request.user, request.POST, initial={'from_user': request.user}) # request.user передается для выборки только товаров конкретного юзера. Реализовано в forms.py
		if form.is_valid():
			order = form.save(commit=False) # ??????????????
			order.from_user = request.user
			print('---------------------')
			print(request.POST)
			print('---------------------')
			order.save()
			form.save_m2m()
			return redirect('home')
	else:
		form = OrderForm(request.user)
	return render(request, 'addwords/newOrder.html', {'form': form})

def ex_product(request, word_id):
	product = Product.objects.get(pk=word_id)
	context = {'product': product}
	#print(User.objects.first().user_words.all())
	return render(request, 'addwords/exactProduct.html', context)


def info(request):
	context = {}
	return render(request, 'addwords/information.html', context)

def users_list(request):
	context = {}
	users = User.objects.all()
	context['users'] = users
	return render(request, "addwords/users.html", context)

# git add -i



# from rest_framework import viewsets

# from .serializers import WordSerializer
# from .models import Word

# class WordViewSet(viewsets.ModelViewSet):
#     """ Он будет обрабатывать GET и POST для Heroe без дополнительной работы. """
#     queryset = Word.objects.all()
#     serializer_class = WordSerializer

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

'''