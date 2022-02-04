from django.shortcuts import render # noqa
from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Olá Django!</body></html>', content_type='text/html')
