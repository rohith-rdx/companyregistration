from xml.dom.minidom import Document
from django.urls import URLPattern, re_path,include
from django.contrib import admin
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path(r'^$', views.index, name="index"),
    re_path(r'^login_page$', views.login_page, name="login_page"),
    re_path(r'^signup$', views.signup, name="signup"),
    re_path(r'^login$', views.login, name="login"),
    re_path(r'^company$', views.company, name="company"),
    re_path(r'^register$', views.register, name="register"),
    re_path(r'^branch$', views.branch, name="branch"),
    re_path(r'^logout$', views.logout, name="logout"),
    
    
    
]
