from primeiraAplicacaoDjango.modulos import views
from django.urls import path

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
]
