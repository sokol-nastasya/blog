from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.video, name = 'video'),
    url(r'video/get/(?P<video_id>\d+)$', views.video_main, name = 'video_main'),
    
    ]