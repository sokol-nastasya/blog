from django.conf.urls import url
from django.contrib.auth.views import (login, logout)


from account import views

urlpatterns = [
	url(r'^login/$', login, {'template_name':'account/login.html'}, name = 'login'),
	url(r'^logout/$', logout, {'template_name':'account/logout.html'}, name = 'logout'),
	url(r'^register/$', views.register, name = 'register'), 
	url(r'^profile/$', views.prof, name = 'prof'),
	url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),
	url(r'^change-password/$', views.change_password, name = 'change_password'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
	
	
]