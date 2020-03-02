from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('f', views.g_name, name='g_name'),
]