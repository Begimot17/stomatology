from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [
    path('<int:id>',views.index, name='index')
]