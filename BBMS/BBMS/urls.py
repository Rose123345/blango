"""
URL configuration for BBMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accountants.urls')),
    path('core/', include('core.urls')),
    path('donars/', include('donars.urls')),
    path('donations/', include('donations.urls')),
    path('inventory/', include('inventory.urls')),
    path('lab/', include('lab.urls')),
    path('notifications_app/', include('notifications_app.urls')),
    path('reports/', include('reports.urls')),
    path('requests_app/', include('requests_app.urls')),    
]
