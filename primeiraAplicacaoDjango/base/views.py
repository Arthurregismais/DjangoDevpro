from django.shortcuts import render # noqa

from primeiraAplicacaoDjango.modulos import facade


def home(request):
    return render(request, 'base/home.html', {'MODULOS': facade.listar_modulos_ordenados()})
