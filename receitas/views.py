from django.shortcuts import render, get_list_or_404, get_object_or_404
from receitas.models import Receita
from django.http import Http404
from django.db.models import Q
from utils.paginacao import cria_paginacao
import os

PER_PAGE = os.environ.get('PER_PAGE', 3)

def inicio(request):
    receitas = Receita.objects.all().order_by('-id')

    page_obj, intervalo_paginacao = cria_paginacao(request,receitas, PER_PAGE)
    return render(request, 'paginas/inicio.html', context={
        'receitas': page_obj,
        'pagina_detalhe': False,
        'intervalo_paginacao': intervalo_paginacao
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
    
    page_obj, intervalo_paginacao = cria_paginacao(request,receitas, PER_PAGE)
    
    return render(request, 'paginas/receita-categoria.html', context={
        'receitas': page_obj,
        'categoria': receitas[0].categoria.nome,
        'pagina_detalhe': False,
        'intervalo_paginacao': intervalo_paginacao
    })
    
def busca(request):
    valor_busca = request.GET.get('q', '').strip()
    if not valor_busca:
        raise Http404()
    
    receitas = Receita.objects.filter(
        Q(titulo__icontains=valor_busca) | Q(descricao__icontains=valor_busca)
    )
    page_obj, intervalo_paginacao = cria_paginacao(request,receitas, PER_PAGE)
    
    return render(request, 'paginas/busca.html', context={
        'pagina_detalhe': False,
        'titulo_pagina': f'Busca por "{valor_busca}" | ',
        'valor_busca': valor_busca,
        'receitas':page_obj,
        'intervalo_paginacao':intervalo_paginacao,
        'consulta_adicional_url': f'&q={valor_busca}'
    })