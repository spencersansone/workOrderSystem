from django.contrib import admin
from django.urls import include
from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.login_user, name='home'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^rl/$', views.requestList, name='requestList'),
    url(r'^user/$', views.userInfo, name="userInfo"),
    url(r'^t/$', views.technicianList, name="technicianList"),
]