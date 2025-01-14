from django.shortcuts import redirect, render
from django.http import Http404,HttpResponse, HttpResponseNotAllowed
from .forms import CadastroForm

def registrar(request):
    dados_formulario = request.session.get('dados_formulario_cadastro', None)
    form = CadastroForm(dados_formulario)
    return render(request, 'autores/paginas/cadastro.html',
                {'form':form})

def cadastro(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['dados_formulario_cadastro'] = POST
    
    form = CadastroForm(POST)
    
    return redirect('autores:registrar')