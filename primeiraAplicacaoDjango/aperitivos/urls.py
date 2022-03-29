from primeiraAplicacaoDjango.aperitivos.views import video
from django.urls import path

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video')
]
