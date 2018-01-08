"""dataone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from webapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
todo_router=routers.DefaultRouter()
#todo_router.register(r'todos', views.directorlist, base_name='todos')
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^director/',views.directorlist.as_view(),name='director'),
    url(r'^leadactor/',views.leadactorslist.as_view(),name='leadactor'),
    url('^$', views.details,name='movie'),
    url(r'^new/',views.test, name='new'),
    url(r'^movielist/',views.movielist.as_view(),name='movielist'),
    url(r'^delete/(?P<id>[0-9]+)/',views.delete_movie, name='delete'),
    url(r'^edit/(?P<id>[0-9]+)/',views.edit_movie, name='edit')
]
