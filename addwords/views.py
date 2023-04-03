from django.shortcuts import render, redirect, HttpResponse
from .models import Word
from django.contrib.auth.decorators import login_required
from .forms import WordForm
from django.contrib.auth.models import User



# Еще одна причина перейти на GET, это то, что GET не должен
# использоваться с методами, которые меняют состояние сервера, 
# а только для read-only операций.

def main(request):
	AMOUNT_OF_WORDS = 15
	if request.GET.get('selecter', False) not in ("None", False):
		sort_name = str(request.GET.get('selecter', False))
		words = Word.objects.filter(archived=False).order_by(sort_name)[:AMOUNT_OF_WORDS] # 
	else:
		words = Word.objects.filter(archived=False)[:AMOUNT_OF_WORDS]
	context = {"words":words}

	return render(request, "addwords/main.html", context)

#@login_required # будет перебрасывать на страницу LOGIN_URL, если юзер не вошел в систему.
# Вы можете сделать то же самое вручную, путём тестирования request.user.is_authenticated, но декоратор намного удобнее!
def new_word(request):
	if request.method == 'POST':
		form = WordForm(request.POST)
		if form.is_valid():
			word = form.save(commit=False)
			word.author = request.user # request.user возвращает текущего пользователя
			word.archived = False
			word.save()
			return redirect('main')
	else:
		form = WordForm()
	return render(request, 'addwords/add.html', {'form': form})

def ex_word(request, word_id):
	word = Word.objects.get(pk=word_id)
	context = {'word': word}
	# print(User.objects.first().user_words.all())
	return render(request, 'addwords/One_word.html', context)


def info(request):
	context = {}
	return render(request, 'addwords/information.html', context)

def users_list(request):
	context = {}
	users = User.objects.all()
	context['users'] = users	
	return render(request, "addwords/users.html", context)





from rest_framework import viewsets

from .serializers import WordSerializer
from .models import Word

class WordViewSet(viewsets.ModelViewSet):
    """ Он будет обрабатывать GET и POST для Heroe без дополнительной работы. """
    queryset = Word.objects.all()
    serializer_class = WordSerializer

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