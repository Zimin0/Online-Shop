from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from addwords.models import Product, Order
from django.contrib.auth.decorators import login_required

from django.db.models import Q, QuerySet

# Create your views here.
def home(request):
    context = {}
    
    if request.user.pk != None: # Если пользователь не Анонимный - т е незарегестрированный
        context = {'user':request.user} ## !!!!!!!!!!!!!!!!!!!11 обработать пустые пост запросы
        if request.method == 'POST': # POST запрос приходит в виде '1.0', где 1 - pk обмена,  0 - status
            order_pk, status = request.POST['status'].split('.')
            curr_order = Order.objects.get(pk=order_pk)
            if status == '1' and curr_order.status == 'IN':
                curr_order.status = 'FI' # меняем статус обмена на совершенный
                to_user = curr_order.to_user # юзер, которому достанется слово
                for prod in curr_order.products.all():
                    prod.seller = to_user
                    prod.save() # update_fields=["name"] # текущее слово (объект), которым меняются пользователи
            else: # если пользователь отклонил заявку или статус заявки уже IN или RE
                curr_order.status = 'RE'
            curr_order.save()

        user_products = Product.objects.filter(seller=request.user.pk)
        q =  Q(from_user=request.user) & Q(status='IN')
        orders = Order.objects.filter(q)
        context['user_products'] = user_products
        context['orders'] = orders
    

    return render(request, "registration/home.html", context)

# class Home(CreateView):
#     template_name = "registration/home.html"

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"  