from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryViews.as_view(), name='category'),
    path('add_news/', add_news, name='add_news'),
    path('read_more/<int:post_id>/', read_more, name='post')
]