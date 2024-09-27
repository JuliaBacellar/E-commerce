from django.urls import path 
from . import views 

urlpatterns = [
    path('listar_produtos', views.listar_produtos)
]