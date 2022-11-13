from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_catalogo, name="index_catalogo"),
    path('autores', views.alta_autores, name="autores_alta"),
    path('usuarios', views.alta_autores, name="usuarios_alta"),
]