from django.shortcuts import render, redirect
from .models import Word
from .forms import WordForm

def main(request):
	AMOUNT_OF_WORDS = 6
	if request.GET.get('selecter', False) not in ("None", False):
		sort_name = str(request.GET.get('selecter', False))
		words = Word.objects.order_by(sort_name)[:AMOUNT_OF_WORDS]
	else:
		words = Word.objects.all()[:AMOUNT_OF_WORDS]

	for w in words: # поменять !!!!!!!!!!!!!1
		if w.type == "n":
			w.type = 'Noun'
		if w.type == "a":
			w.type = "Adjective"
		if w.type == "v":
			w.type = "Verb"


	
	context = {"words":words}
	return render(request=request, template_name="addwords/main.html", context=context)

def new_word(request):
	if request.method == 'POST':
		form = WordForm(request.POST)
		if form.is_valid():
			word = form.save(commit=False)
			word.save()
			return redirect('main')
	else:
		form = WordForm()
	return render(request, 'addwords/add.html', {'form': form})

