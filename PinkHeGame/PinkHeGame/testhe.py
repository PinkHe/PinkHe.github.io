from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

def hello(request):
    return HttpResponse("Hello world ! hahah")

def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, './templates/index.html', context)