from django import forms
from .models import Word


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('word', 'language', 'type', 'translation', 'discription')
