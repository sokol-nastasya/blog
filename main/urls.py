from django.conf.urls import url, include
from . import views
from main.views import MySearchView

urlpatterns = [
    url(r'^$', views.main, name = 'main'),
    url(r'^/search/?$', MySearchView.as_view(), name='search_view'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^contact/$', views.contact, name = 'contact'),
    url(r'^calendar/$', views.calendar, name = 'calendar'),
    url(r'^media/$', views.media, name = 'media'), 
    url(r'^certificates/$', views.certificates, name = 'certificates'),
    url(r'^photo_doctor/$', views.photo, name = 'photo_doctor'),
    
]
