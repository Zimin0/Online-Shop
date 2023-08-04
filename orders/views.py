from django.shortcuts import render, redirect
from orders.forms import OrderForm

def new_order(request):
	"""Добавление нового заказа."""
	if request.method == 'POST':
		form = OrderForm(request.user, request.POST, initial={'from_user': request.user}) # request.user передается для выборки только товаров конкретного юзера. Реализовано в forms.py
		if form.is_valid():
			order = form.save(commit=False) # метод save вернет экземпляр модели, но не сохранит его в базе данных
			order.from_user = request.user
			order.save()
			form.save_m2m() # сохраняет m2m поля, нужен только при вызове save(commit=False)
			return redirect('users:home')
	else:
		form = OrderForm(request.user)
	return render(request, 'orders/newOrder.html', {'form': form})
