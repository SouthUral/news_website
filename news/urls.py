from django.urls import path
from .views import *


urlpatterns = [
    path('', index_news, name='home'),
    path('category/<int:category_id>/', category_, name='category'),
    path('add_news/', add_news, name='add_news'),
    path('read_more/<int:post_id>/', read_more, name='post')
]