from .models import PrepositionalNews
from django.forms import ModelForm, TextInput, ImageField, Textarea


class PrepositionalNewsForm(ModelForm):
    class Meta:
        model = PrepositionalNews
        fields = ['title', 'anons', 'image', 'full_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }
