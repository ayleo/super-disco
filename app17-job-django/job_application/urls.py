from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # Specify the path (in this case '' is empty as it is the homepage)
    # call the index function from views.py
    # name the path 'index'
]