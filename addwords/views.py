from django.shortcuts import render, redirect
from .models import Word
from .forms import WordForm

def main(request):
	words = Word.objects.all()
	for w in words:
		#w.synonyms.set(list(*[sy for sy in w.synonyms.all()]))
		#print(*[i for i in w.synonyms.all()])
		#print(w.synonyms)
		#print(w.synonyms)
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
