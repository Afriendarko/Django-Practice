from django.urls import path
from . import views
urlpatterns = [
    path('success', views.index, name='index'),
    path('t', views.teapp, name='teapp'),
    path('f', views.get_name, name='get_name'),
    path('f2', views.modform, name='modform'),
    path('songs/', views.ListSongsView.as_view(), name='songs-all'),
]