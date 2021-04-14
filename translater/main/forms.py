from .models import Words
from django.forms import ModelForm, TextInput

class WordsForm(ModelForm):
    class Meta:
        model = Words 
        fields = ['word', 'translated_word']

        widgets = {
            'word': TextInput(attrs={
                'name':'search',
                'class': 'form-control',
                'placeholder': 'Введите слово'
            }),
            'translated_word': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите перевод слова'
            }),
        }

