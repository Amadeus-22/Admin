from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('myapp/index.html')
    return render(request, 'myapp/index.html')
