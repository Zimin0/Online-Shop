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
    context = {'user':request.user}
    if request.method == 'POST': # POST запрос приходит в виде '1.0', где 1 - pk обмена,  0 - status
        exchange_pk, status = request.POST['status'].split('.')
        if status == '1':
            curr_exch = Exchange.objects.filter(pk=exchange_pk)
            curr_exch.update(status="AC") # меняем статус обмена на совершенный
            to_user = curr_exch[0].to_user # юзер, которому достанется слово
            curr_word = QuerySet(curr_exch[0].word) # текущее слово (объект), которым меняются пользователи
            curr_word.update(author=to_user)
        else:
            print(1)


    
    author_words = Word.objects.filter(author=request.user.pk)
    q = Q(from_user=request.user) | Q(to_user=request.user)
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