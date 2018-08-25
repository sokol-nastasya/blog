from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.article_cat, name = 'article_cat'), 
    url(r'^article/get/(?P<article_id>\d+)/$', views.article, name = 'article'),
    url(r'^category/get/(?P<category_id>\d+)/$', views.category, name = 'category'),
]