from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [
    path('<int:id>',views.index, name='index'),
    path('print_info/<int:id>',views.print_info, name='print_info')
]