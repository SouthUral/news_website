from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.


class HomeViews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class CategoryViews(HomeViews):
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        filter_field = {'category_id': self.kwargs['category_id'], 'is_published': True}
        return News.objects.filter(**filter_field)

# def index_news(request):
#     news = News.objects.exclude(is_published=False)
#     header = 'Список новостей'
#     context = {
#         'title': header,
#         'news': news
#     }
#     # news_list = ''.join([f'  <p>{obj.id} | {obj.title}: {obj.content}</p>\n' for obj in news])
#     return render(request, 'news/index.html', context)


# def category_(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'title': category,
#         'news': news,
#     }
#     return render(request, 'news/index.html', context)


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})


# def read_more(request, post_id):
#     news = get_object_or_404(News, pk=post_id)
#     # news = News.objects.get(pk=post_id)
#     context = {
#         'news': news,
#     }
#     return render(request, 'news/read_more.html', context)

class ViewNews(DetailView):
    model = News
    template_name = 'news/read_more.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'news'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
