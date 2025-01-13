from django.shortcuts import render
from .forms import CadastroForm

def cadastro(request):
    form = CadastroForm()
    return render(request, 'autores/paginas/cadastro.html',
                {'form':form})
