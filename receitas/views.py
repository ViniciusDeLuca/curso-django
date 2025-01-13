from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.receitas.factory import gerar_receita_ficticia
from pprint import pprint
from receitas.models import Receita, Categoria
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from utils.paginacao import cria_paginacao

def inicio(request):
    receitas = Receita.objects.all().order_by('-id')

    current_page = request.GET.get('page', 3)
    paginator = Paginator(receitas, 3)
    page_obj = paginator.get_page(current_page)
    
    intervalo_paginacao = cria_paginacao(
        paginator.page_range,
        4,
        int(current_page)
    )
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
    
    return render(request, 'paginas/receita-categoria.html', context={
        'receitas': receitas,
        'categoria': receitas[0].categoria.nome,
        'pagina_detalhe': False
    })
    
def busca(request):
    valor_busca = request.GET.get('q', '').strip()
    if not valor_busca:
        raise Http404()
    
    receitas = Receita.objects.filter(
        Q(titulo__icontains=valor_busca) | Q(descricao__icontains=valor_busca)
    )
    return render(request, 'paginas/busca.html', context={
        'pagina_detalhe': False,
        'titulo_pagina': f'Busca por "{valor_busca}" | ',
        'valor_busca': valor_busca,
        'receitas':receitas
    })