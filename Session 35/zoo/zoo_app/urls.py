from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.species_list, name='list'),
    path('add', views.add_species, name='add_species'),
]
