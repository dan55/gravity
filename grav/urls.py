"""grav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from gravapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'index', views.index, name='index'),        
    url(r'^admin/', admin.site.urls),
    url(r'create_character', views.create_character, name='create_character'),
    url(r'delete_character', views.delete_character, name='delete_character'),
    url(r'create_relationship', views.create_relationship, name='create_relationship'),
    url(r'delete_relationship', views.delete_relationship, name='delete_relationship'),
]