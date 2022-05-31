from django.urls import path
from . import views

app_name = 'stage4'

urlpatterns = [
    path('<int:id>',views.index, name='index')
]
