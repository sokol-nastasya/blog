from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.news_page, name = 'news_page'),
	url(r'^news/(?P<show_news_id>[0-9]+)/$', views.show_news_page, name = 'news'),
	url(r'^keywords/(?P<k_id>[0-9]+)/$', views.keywords, name = 'keywords'),
]
