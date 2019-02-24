from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='name'),
    path('name/', views.name, name='name'),
    path('<int:num>/', views.cube, name='cube'),
    path('', views.index, name='index'),
]