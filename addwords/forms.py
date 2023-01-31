from django import forms
from .models import Word


class WordForm(forms.ModelForm):
    template_name = "addwords/new_form.html" # only since Django4
    class Meta:
        model = Word
        fields = ('word', 'language', 'type', 'translation', 'discription')
