from typing import List

from primeiraAplicacaoDjango.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista modulos ordenados por título
    :return:
    """

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str):
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())
