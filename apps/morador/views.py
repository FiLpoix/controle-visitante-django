from django.shortcuts import render
from morador.models import Morador

# Create your views here.

def informacoes_morador(request):
    todos_moradores = Morador.objects.order_by('nome_completo')

    context = {
        'nome_pagina': 'Inicio moradores',
        'todos_moradores': todos_moradores
    }

    return render(request, 'informacoes_morador.html', context)