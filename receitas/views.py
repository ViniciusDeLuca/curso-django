from django.shortcuts import render, get_list_or_404
from utils.receitas.factory import gerar_receita_ficticia
from pprint import pprint
from receitas.models import Receita, Categoria

def inicio(request):
    receitas = Receita.objects.all().order_by('-id')

    return render(request, 'paginas/inicio.html', context={
        'receitas': receitas,
        'pagina_detalhe': False
    })

def receitaDetalhe(request, id):
    receita = Receita.objects.filter(id=id).first()

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