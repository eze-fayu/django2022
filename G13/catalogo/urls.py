from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_catalogo, name="index_catalogo"),
    path('autores', views.alta_autores, name="autores_alta"),
    path('usuarios', views.alta_usuarios, name="alta_usuario"),
    path('libros', views.alta_libros, name="alta_libros"),
    path('ejemplares', views.alta_ejemplares, name="alta_ejemplares"),
    path('prestamos', views.prestamos, name="prestamos"),
    path('devoluciones', views.devoluciones, name="devoluciones"),
    path('reservas', views.reservas, name="reservas"),
    path('consultas/<str:apellido>', views.consultas, name="consultas"),
]