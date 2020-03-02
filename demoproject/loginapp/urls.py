from django.urls import path
from . import views

urlpatterns = [
    path('success', views.index, name='index'),
    path('login', views.user_login, name='login'),
]