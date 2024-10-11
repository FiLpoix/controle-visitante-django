from django.shortcuts import render
from .models import Morador

# Create your views here.

def moradores(request):
    moradores = Morador.objects.order_by('nome_completo')

    context = {
        'nome_pagina': 'Inicio moradores',
        'moradores': moradores
    }

    return render(request, 'moradores.html', context)