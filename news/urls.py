from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryViews.as_view(), name='category'),
    path('add_news/', CreateNews.as_view(), name='add_news'),
    path('read_more/<int:post_id>/', ViewNews.as_view(), name='post')
]