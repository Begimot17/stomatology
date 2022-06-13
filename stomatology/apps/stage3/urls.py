from django.urls import path
from . import views

app_name = 'stage3'

urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('update/<int:id>', views.update, name='update'),
    path('print_info/<int:id>',views.print_info, name='print_info')
]
