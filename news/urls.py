from django.urls import path
from .views import *


urlpatterns = [
    path('', index_news, name='home'),
    path('category/<int:id_category>/', category_, name='category'),
    path('add_news/', add_news, name='add_news'),
    path('read_more/<int:id_news>/', read_more, name='read_more')
]