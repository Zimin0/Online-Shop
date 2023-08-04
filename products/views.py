from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product, Category
from django.db.models import Q, Count
from products.forms import ProductForm

def ex_product(request, word_id):
	""" Страница конкретного товара. """
	product = get_object_or_404(Product.objects.select_related('category'), pk=word_id)
	context = {'product': product}
	return render(request, 'products/exactProduct.html', context)

def ex_category(request, category_id):
	""" Выбраная категория товаров """
	context = {}
	AMOUNT_OF_PRODUCTS = 15
	current_category = Category.objects.get(pk=category_id) # получение текущей выбраной категории
	q = Q(archived=False) & Q(category=current_category) # Выборка неархивированой записи и записи из требуемой категории
	categories = Category.objects.all().order_by("name")

	if request.GET.get('selecter', False) not in ("None", False):
		sort_name = str(request.GET.get('selecter', False))
		products = Product.published.filter(q).order_by(sort_name)[:AMOUNT_OF_PRODUCTS] # Используется менеджер published. Подробнее написано в моделях.
	else:
		products = Product.published.filter(q)[:AMOUNT_OF_PRODUCTS]

	current_cat = Category.objects.get(pk=category_id)
	context = {
		"products":products,
		"categories":categories,
		"current_cat":current_cat,
		}
	return render(request, "catalog/main.html", context)

# @login_required будет перебрасывать на страницу LOGIN_URL, если юзер не вошел в систему.
# Вы можете сделать то же самое вручную, путём тестирования request.user.is_authenticated, но декоратор намного удобнее!
def new_product(request):
	"""Добавление товара заказа."""
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES) # request.FILES - для загрузки файлов
		if form.is_valid():
			product = form.save(commit=False)
			product.seller = request.user # request.user возвращает текущего пользователя
			product.save(update_fileds=['seller']) 
			return redirect('main')
	else:
		form = ProductForm()
	return render(request, 'products/newOrder.html', {'form': form}) 
