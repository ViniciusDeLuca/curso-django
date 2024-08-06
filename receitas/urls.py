from django.urls import path
from receitas.views import home, sobre, contatos

urlpatterns = [
    path('', home), 
    path('sobre/', sobre), 
    path('contato/', contatos), 
]