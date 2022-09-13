from django import forms
from .models import Category

class NewsForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=255)
    content = forms.CharField(label='Контент')
    is_published = forms.BooleanField(required=False, label='Опубликовать?')
    category = forms.ModelChoiceField(label='Выберите категорию', empty_label='Категория', queryset=Category.objects.all())