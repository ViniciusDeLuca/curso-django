from django.shortcuts import render

def home(request):
    receita = 'Bolo de morango'
    return render(request, 'home.html', context={
        'receita': receita
    })
