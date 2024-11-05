from django.shortcuts import render
from gerar_receitas import gerar_receita_ficticia
def home(request):
    return render(request, 'paginas/home.html', context={
        'receitas': [gerar_receita_ficticia() for _ in range(18)],
    })

def receitaDetail(request, id):
    return render(request, 'paginas/receita-detail.html', context={
        'receita': gerar_receita_ficticia()
    })