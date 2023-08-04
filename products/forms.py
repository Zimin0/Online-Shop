from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    #template_name = "addwords/new_form.html" # only since Django4
    class Meta:
        model = Product
        fields = ('name', 'category', 'discription', 'price', 'img') # можно '__all__'