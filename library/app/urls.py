from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('details/<int:book_id>/',views.details,name="details"),
    path('modifier/<int:book_id>/',views.modif,name="modifier"),
    path('mod_details/<int:book_id>/',views.mod_details,name="mod_details"),
    path('supp/<int:book_id>/',views.supp,name="supp"),
    path('ajouter/',views.ajouter,name="ajouter"),
    path('rech/',views.rech,name='rech')
]