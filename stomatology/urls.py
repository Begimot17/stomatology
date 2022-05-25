"""stomatology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
    path('', include('authorize.urls')),
    path('analysis/', include('analysis.urls')),
    path('materials/', include('materials.urls')),
    path('patients/', include('patients.urls')),
    path('timetable/', include('timetable.urls')),
    path('stage1/', include('stage1.urls')),
    path('stage2/', include('stage2.urls')),
    path('stage3/', include('stage3.urls')),
    path('stage4/', include('stage4.urls')),
    path('card/', include('card.urls')),
    path('admin/', admin.site.urls),
]