from django.urls import path, include
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.list, name='posts'),
    path('<int:id>', views.detail, name='detail')
] 