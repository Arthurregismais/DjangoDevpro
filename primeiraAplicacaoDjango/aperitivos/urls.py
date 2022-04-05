from primeiraAplicacaoDjango.aperitivos.views import video, indice
from django.urls import path

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', indice, name='indice')
]
