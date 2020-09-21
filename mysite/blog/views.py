from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Post, Evento

def index(request):
    objetos = Post.objects.filter().all()
    eventos = Evento.objects.filter().all()

    return render(request, 'index.html', context={'posts':objetos, 'eventos': eventos})

def news(request):
    objetos = Post.objects.filter().all()

    return render(request, 'news.html', context={'posts':objetos})

def evento(request):
    objetos = Evento.objects.filter().all()

    return render(request, 'events.html', context={'eventos':objetos})