from django.urls import path

from .views import index, news, evento
urlpatterns = [
    path('index', index, name='index'),
    path('news', news, name="news" ),
    path('eventos', evento, name="eventos")
]