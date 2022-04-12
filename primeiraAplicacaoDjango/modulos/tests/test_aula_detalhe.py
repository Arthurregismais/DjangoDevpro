from django.urls import reverse
import pytest
from model_mommy import mommy
# from django.test import Client

from primeiraAplicacaoDjango.django_assertions import assert_contains
from primeiraAplicacaoDjango.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo_da_aula(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_aula_vimeo(resp, aula: Aula):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ aula.vimeo_id }')


def test_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{ modulo.get_absolute_url()}">{ modulo.titulo }</a'
                          f'></li>')


def test_link_modulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.get_absolute_url())
