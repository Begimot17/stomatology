from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('',views.index, name='index'),
    path('add/',views.add, name='add'),
    path('reg/',views.reg, name='reg'),
    path('update/<int:id>',views.update, name='update')
]
