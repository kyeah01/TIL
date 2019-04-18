from django.urls import path
from . import views

urlpatterns = [
    path('ans/', views.ans, name='ans'),
    path('name/', views.form_a, name='name'),
    path('redirect/',  views.redirection),
    path('', views.index, name='index'),
]