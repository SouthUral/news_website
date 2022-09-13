from django.shortcuts import render, get_object_or_404
from .models import News, Category


# Create your views here.


def index_news(request):
    news = News.objects.exclude(is_published=False)
    header = 'Список новостей'
    context = {
        'title': header,
        'news': news
    }
    # news_list = ''.join([f'  <p>{obj.id} | {obj.title}: {obj.content}</p>\n' for obj in news])
    return render(request, 'news/index.html', context)


def category_(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'title': category,
        'news': news,
    }
    return render(request, 'news/index.html', context)


def add_news(request):
    return render(request, 'news/add_news.html')


def read_more(request, post_id):
    news = get_object_or_404(News, pk=post_id)
    # news = News.objects.get(pk=post_id)
    context = {
        'news': news,
    }
    return render(request, 'news/read_more.html', context)
