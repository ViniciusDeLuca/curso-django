from django.shortcuts import render
from utils.receitas.factory import gerar_receita_ficticia
from pprint import pprint

def inicio(request):
    receitas = [gerar_receita_ficticia() for _ in range(18)]

    return render(request, 'paginas/inicio.html', context={
        'receitas': receitas,
        'pagina_detalhe': False
    })

def receitaDetalhe(request, id):
    return render(request, 'paginas/receita-detalhe.html', context={
        'receita': gerar_receita_ficticia(),
        'pagina_detalhe': True
    })