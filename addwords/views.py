from django.shortcuts import render
from .models import Word
from .forms import WordForm
from django.http import HttpResponse

def main(request):
	words = Word.objects.all()
	for w in words:
		
		if w.type == "n":
			w.type = 'Noun'
		if w.type == "a":
			w.type = "Adjective"
		if w.type == "v":
			w.type = "Verb"
	
	context = {"words":words}
	return render(request=request, template_name="addwords/main.html", context=context)

def new_word(request):
	form = WordForm()
	#return HttpResponse("<h1>HELLO NEW WORD! </h1>")
	context = {} 
	return render(request, 'addwords/add.html', context)
