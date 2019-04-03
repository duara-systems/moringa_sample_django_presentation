from django.urls import path

from . import views
name = 'Landing'
urlpatterns = [
    path('', views.index, name= 'index'),
]