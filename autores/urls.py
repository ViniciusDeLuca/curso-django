from django.urls import path
from . import views

app_name = 'autores'

urlpatterns = [
    path('registro/', views.registrar, name='registrar'),
    path('registro/cadastro/', views.cadastro, name='cadastro'),
]