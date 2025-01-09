from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.receitas.factory import gerar_receita_ficticia
from pprint import pprint
from receitas.models import Receita, Categoria
from django.http import Http404

def inicio(request):
    receitas = Receita.objects.all().order_by('-id')

    return render(request, 'paginas/inicio.html', context={
        'receitas': receitas,
        'pagina_detalhe': False
    })

def receitaDetalhe(request, id):
    receita = get_object_or_404(
        Receita, id=id
    )

    return render(request, 'paginas/receita-detalhe.html', context={
        'receita': receita,
        'pagina_detalhe': True
    })

def receitaCategoria(request, categoria_id):
    receitas = get_list_or_404(
        Receita.objects.filter(categoria__id=categoria_id).order_by('-id')
    )
    
    return render(request, 'paginas/receita-categoria.html', context={
        'receitas': receitas,
        'categoria': receitas[0].categoria.nome,
        'pagina_detalhe': False
    })
    
def busca(request):
    valor_busca = request.GET.get('q', '').strip()
    if not valor_busca:
        raise Http404()
    return render(request, 'paginas/busca.html', context={
        'pagina_detalhe': False,
        'titulo_pagina': f'Busca por "{valor_busca}" | ',
        'valor_busca': valor_busca
    })