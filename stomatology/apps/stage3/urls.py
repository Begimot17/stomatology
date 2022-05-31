from django.urls import path
from . import views

app_name = 'stage3'

urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('update/<int:id>', views.update, name='update')
]
