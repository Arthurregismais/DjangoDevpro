from primeiraAplicacaoDjango.modulos import facade
from model_mommy import mommy
from primeiraAplicacaoDjango.modulos.models import Modulo
import pytest


@pytest.fixture
def modulos(db):
    return [mommy.make(Modulo, titulo=s) for s in "Antes Depois".split()]


def test_listar_modulos_ordenados(modulos):
    assert list(sorted(modulos, key=lambda modulo: modulo.titulo)) == facade.listar_modulos_ordenados()
