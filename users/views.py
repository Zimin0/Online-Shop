from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from addwords.models import Word, Exchange
from django.contrib.auth.decorators import login_required

from django.db.models import Q, QuerySet

# Create your views here.
def home(request):
    print("-----------------------------------")
    print(request.user.pk)
    print("-----------------------------------")
    context = {}
    
    if request.user.pk != None: # Если пользователь не Анонимный - т е незарегестрированный
        context = {'user':request.user} ## !!!!!!!!!!!!!!!!!!!11 обработать пустые пост запросы
        if request.method == 'POST': # POST запрос приходит в виде '1.0', где 1 - pk обмена,  0 - status
            exchange_pk, status = request.POST['status'].split('.')
            curr_exch = Exchange.objects.get(pk=exchange_pk)
            if status == '1' and curr_exch.status == 'IN':
                curr_exch.status = 'AC' # меняем статус обмена на совершенный
                to_user = curr_exch.to_user # юзер, которому достанется слово
                curr_word = curr_exch.word # текущее слово (объект), которым меняются пользователи
                curr_word.author = to_user
                curr_word.save() # update_fields=["name"]
            else: # если пользователь отклонил заявку или статус заявки уже IN или RE
                curr_exch.status = 'RE'
            curr_exch.save()

        author_words = Word.objects.filter(author=request.user.pk)
        q =  Q(from_user=request.user) & Q(status='IN')
        exchanges = Exchange.objects.filter(q)
        context['author_words'] = author_words
        context['exchanges'] = exchanges
    

    return render(request, "registration/home.html", context)

# class Home(CreateView):
#     template_name = "registration/home.html"

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"  