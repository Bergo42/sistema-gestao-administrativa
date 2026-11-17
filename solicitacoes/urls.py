from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_solicitacoes, name='listar_solicitacoes'),
    path('cadastrar/', views.cadastrar_solicitacao, name='cadastrar_solicitacao'),
]