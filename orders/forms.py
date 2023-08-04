from django import forms
from django.contrib.auth.models import User

from products.models import Product
from orders.models import Order

class OrderForm(forms.ModelForm):
    #template_name = "addwords/new_form.html" # only since Django4
    def __init__(self, User_model, *args, **kwargs): # Реализация вывода в форму только товаров конкретного юзера.
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['products'].queryset = Product.objects.filter(seller=User_model)
        self.fields['to_user'].queryset = User.objects.exclude(pk=User_model.pk)

    class Meta:
        model = Order
        fields = ('products','to_user')

