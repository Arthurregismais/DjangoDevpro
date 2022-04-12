from primeiraAplicacaoDjango.turmas import views
from django.urls import path

app_name = 'turmas'
urlpatterns = [
    path('', views.indice, name='indice'),
]
