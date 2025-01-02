from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('receita/<int:id>/', views.receitaDetalhe, name="receita_detalhe"),
]