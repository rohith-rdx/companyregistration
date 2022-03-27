from xml.dom.minidom import Document
from django.urls import URLPattern, re_path,include
from django.contrib import admin
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path(r'^branchregistration$', views.branchregistration, name="branchregistration"),
    re_path(r'^branchreg$', views.branchreg, name="branchreg"),
    re_path(r'^branchlogin$', views.branchlogin, name="branchlogin"),
    re_path(r'^branchlog$', views.branchlog, name="branchlog"),
    re_path(r'^employeregistration$', views.employeregistration, name="employeregistration"),
    re_path(r'^employeereg$', views.employeereg, name="employeereg"),
    re_path(r'^employeeshow$', views.employeeshow, name="employeeshow"),
    re_path(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    re_path(r'^empedit/(?P<id>\d+)$', views.empedit, name='empedit'),
    re_path(r'^update/(?P<id>\d+)$', views.update, name='update'),
    re_path(r'^logout$', views.logout, name="logout"),
]
