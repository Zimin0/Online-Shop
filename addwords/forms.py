from django import forms
from .models import Product, Order
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    template_name = "addwords/new_form.html" # only since Django4
    class Meta:
        model = Product
        fields = ('name', 'category', 'discription', 'price', 'img') # можно '__all__


class OrderForm(forms.ModelForm):

    template_name = "addwords/new_form.html" # only since Django4
    class Meta:
        model = Order
        fields = ('products', 'from_user', 'to_user')

