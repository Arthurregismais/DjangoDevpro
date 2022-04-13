from primeiraAplicacaoDjango.modulos import facade
from django.shortcuts import render


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})


def indice(request):
    ctx = {'modulos': facade.listar_modulos_com_aulas}
    return render(request, 'modulos/indice.html', ctx)