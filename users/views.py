from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from addwords.models import Word
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context = {'user':request.user}
    
    author_words = Word.objects.filter(author=request.user.pk)
    context['author_words'] = author_words

    return render(request, "registration/home.html", context)

# class Home(CreateView):
#     template_name = "registration/home.html"

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"  