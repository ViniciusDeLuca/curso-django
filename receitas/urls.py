from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('receita/categoria/<int:categoria_id>/', views.receitaCategoria, name="receitas_por_categorias"),
    path('receita/<int:id>/', views.receitaDetalhe, name="receita_detalhe"),
]