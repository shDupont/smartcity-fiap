import django
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    primeiroNome = models.CharField(max_length=60)
    segundoNome = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    senha = models.CharField(max_length=20)


class Post(models.Model):
    titulo = models.CharField(max_length=60)
    textoCorpo = models.CharField(max_length=2000)
    dataHoraEvento = models.DateTimeField(editable=True, default=django.utils.timezone.now)
    bannerEvento = models.ImageField(upload_to='blog/media')


class Evento(models.Model):
    tipoEvento = models.CharField(max_length=60)
    tituloEvento = models.CharField(max_length=240)
    date = models.DateTimeField(editable=True, default=django.utils.timezone.now)




