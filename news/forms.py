from django import forms
from .models import News

# class NewsForm(forms.Form):
#     title = forms.CharField(label='Заголовок', max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={"class": "form-control"}))
#     is_published = forms.BooleanField(required=False, label='Опубликовать?', initial=True)
#     category = forms.ModelChoiceField(label='Категория', empty_label='Выберите категорию', queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'content',
            'is_published',
            'category', 
        ]
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-conrol"}),
        }