import pytest
from django.test import TestCase
from django.urls import reverse

from primeiraAplicacaoDjango.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1> Video Aperitivo: Motivação </h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/693299473?h=896429f7a1&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" width="1280" height="720" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="AULA 01 - MOTIVA&amp;Ccedil;&amp;Atilde;O &amp;mdash; Curso de Python Gr&amp;aacute;tis"></iframe>')
