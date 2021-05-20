"""EzE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views


urlpatterns = [
    path('', views.dashboard ,name='events-home'),
    path('account/', views.account ,name='events-account'),
    path('create_event', views.create_event,name='create_event'),
    path('update_event/<str:pk>', views.update_event,name='update_event'),
    path('event_detail/<str:pk>', views.event_detail,name='event_detail')
]
