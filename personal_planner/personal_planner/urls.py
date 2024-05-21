"""
URL configuration for personal_planner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from django.shortcuts import redirect


from website.views import welcome, date, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('welcome.html')), 
    path('welcome.html', welcome, name="welcome"),
    path('date', date),
    path('about', about),
    path('meetings/', include('meetings.urls'))
]
