from django.shortcuts import render
from gerar_receitas import gerar_receita_ficticia
from pprint import pprint

def home(request):
    receitas = [gerar_receita_ficticia() for _ in range(18)]

    return render(request, 'paginas/home.html', context={
        'receitas': receitas,
    })

def receitaDetail(request, id):
    return render(request, 'paginas/receita-detalhe.html', context={
        'receita': gerar_receita_ficticia()
    })