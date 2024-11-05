from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('receita/<int:id>/', views.receitaDetail),
]