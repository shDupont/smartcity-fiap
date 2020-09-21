from django.contrib import admin

from .models import Usuario, Post, Evento

admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Evento)