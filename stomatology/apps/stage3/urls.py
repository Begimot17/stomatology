from django.urls import path
from . import views

app_name = 'stage3'

urlpatterns = [
    path('',views.index, name='index')
]
