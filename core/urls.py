from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('create/', views.Cadastrar, name='cadastrar'),    
    path('deletar/<str:id>/', views.Deletar, name='deletar'),
    path('atualizar/<str:id>/', views.Atualizar, name='atualizar'),
    path('ConfirmarAtt',views.ConfirmarAtt,name='ConfirmarAtt')

]