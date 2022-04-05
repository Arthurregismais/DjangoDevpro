from typing import List

from primeiraAplicacaoDjango.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista modulos ordenados por título
    :return:
    """

    return list(Modulo.objects.order_by('titulo').all())
