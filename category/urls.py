from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.cat, name = 'cat'),
    url(r'^domestic/$', views.domestic, name = 'domestic'),
    url(r'^bacteria/$', views.bacteria, name = 'bacteria'),
    url(r'^cold/$', views.cold, name = 'cold'),
    url(r'^food/$', views.food, name = 'food'), 
    url(r'^pills/$', views.pills, name = 'pills'),
    url(r'^plants/$', views.plants, name = 'plants'), 
    url(r'^asit/$', views.asit, name = 'asit'), 
    url(r'^asthma/$', views.asthma, name = 'asthma'), 
    url(r'^child/$', views.child, name = 'child'),
    url(r'^t_al/$', views.t_al, name = 't_al'),

    
    
]
