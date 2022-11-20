from django.contrib import admin
from catalogo.models import autores, libros, ejemplares, usuarios, prestamos, devoluciones, reservas
# Register your models here.

admin.site.register(autores)
admin.site.register(libros)
admin.site.register(ejemplares)
admin.site.register(usuarios)
admin.site.register(prestamos)
admin.site.register(devoluciones)
admin.site.register(reservas)

