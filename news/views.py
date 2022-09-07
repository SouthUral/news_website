from django.shortcuts import render
from .models import News, Category


# Create your views here.
def get_category():
    category = Category.objects.all()
    return category

def index_news(request):
    news = News.objects.exclude(is_published=False)
    categories = get_category()
    header = 'Список новостей'
    context = {
        'categories': categories,
        'title': header,
        'news': news
    }
    # news_list = ''.join([f'  <p>{obj.id} | {obj.title}: {obj.content}</p>\n' for obj in news])
    return render(request, 'news/index.html', context)


def category_(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    categories = get_category()
    context = {
        'categories': categories,
        'title': category,
        'news': news,
    }
    return render(request, 'news/index.html', context)


def add_news(request):
    categorys = get_category()
    context = {
        'categorys': categorys
    }
    return render(request, 'news/add_news.html', context)


def read_more(request, post_id):
    news = News.objects.get(pk=post_id)
    context = {
        'news': news,
    }
    return render(request, 'news/read_more.html', context)
