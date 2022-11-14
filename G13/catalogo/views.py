from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Autores_Form, Usuarios_Form, Libros_Form, Ejemplares_Form, Prestamos_Form, Devoluciones_Form, Reservas_Form

# Create your views here.

def index_catalogo(request):
    return render(request, "catalogo/index.html")
    
def alta_autores(request):

    if request.method == "POST":
        autores_form = Autores_Form(request.POST)
        if autores_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            autores_form.save()
            messages.success(request, "Autor Registrado correctamente")
            # autores_form = Autores_Form()
            return render(request, "catalogo/alta_plantilla.html", {'formulario': autores_form, 'tipoalta': 'Autor', 'vinculo': 'autores_alta'})
    else:
        autores_form = Autores_Form()
        return render(request, "catalogo/alta_plantilla.html", {'formulario': autores_form, 'tipoalta': 'Autor', 'vinculo': 'autores_alta'})

def alta_usuarios(request):

    if request.method == "POST":
        usuarios_form = Usuarios_Form(request.POST)
        if usuarios_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            usuarios_form.save()

            messages.success(request, "Usuario Registrado correctamente")

            return render(request, "catalogo/alta_plantilla.html", {'formulario': usuarios_form, 'tipoalta': 'Usuario', 'vinculo': 'alta_usuario'})
    else:
        usuarios_form = Usuarios_Form()
        return render(request, "catalogo/alta_plantilla.html", {'formulario': usuarios_form, 'tipoalta': 'Usuario', 'vinculo': 'alta_usuario'})

def alta_libros(request):

    if request.method == "POST":
        libros_form = Libros_Form(request.POST)
        if libros_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            libros_form.save()

            messages.success(request, "Autor Registrado correctamente")

            return render(request, "catalogo/alta_plantilla.html", {'formulario': libros_form, 'tipoalta': 'Libros', 'vinculo': 'alta_libros'})
    else:
        libros_form = Libros_Form()
        return render(request, "catalogo/alta_plantilla.html", {'formulario': libros_form, 'tipoalta': 'Libros', 'vinculo': 'alta_libros'})

def alta_ejemplares(request):

    if request.method == "POST":
        ejemplares_form = Ejemplares_Form(request.POST)
        if ejemplares_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            ejemplares_form.save()

            messages.success(request, "Autor Registrado correctamente")

            return render(request, "catalogo/alta_plantilla.html", {'formulario': ejemplares_form, 'tipoalta': 'Ejemplares', 'vinculo': 'alta_ejemplares'})
    else:
       ejemplares_form = Ejemplares_Form()
       return render(request, "catalogo/alta_plantilla.html", {'formulario': ejemplares_form, 'tipoalta': 'Ejemplaress', 'vinculo': 'alta_ejemplares'})

def prestamos(request):

    if request.method == "POST":
        prestamo_form = Prestamos_Form(request.POST)
        if prestamo_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            prestamo_form.save()

            messages.success(request, "Autor Registrado correctamente")

            return render(request, "catalogo/alta_plantilla.html", {'formulario': prestamo_form, 'tipoalta': 'Prestamos', 'vinculo': 'prestamos'})
    else:
        prestamo_form = Prestamos_Form()
        return render(request, "catalogo/alta_plantilla.html", {'formulario': prestamo_form, 'tipoalta': 'Prestamos', 'vinculo': 'prestamos'})

def devoluciones(request):

    if request.method == "POST":
        devoluciones_form = Devoluciones_Form(request.POST)
        if devoluciones_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            devoluciones_form.save()

            messages.success(request, "Autor Registrado correctamente")

            return render(request, "catalogo/alta_plantilla.html", {'formulario': devoluciones_form, 'tipoalta': 'Devoluciones', 'vinculo': 'devoluciones'})
    else:
        devoluciones_form = Devoluciones_Form()
        return render(request, "catalogo/alta_plantilla.html", {'formulario': devoluciones_form, 'tipoalta': 'Devoluciones', 'vinculo': 'devoluciones'})

def reservas(request):

    if request.method == "POST":
        reservas_form = Reservas_Form(request.POST)
        if reservas_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            reservas_form.save()

            messages.success(request, "Autor Registrado correctamente")

            return render(request, "catalogo/alta_plantilla.html", {'formulario': reservas_form, 'tipoalta': 'Reservas', 'vinculo': 'reservas'})
    else:
        reservas_form = Reservas_Form()
        return render(request, "catalogo/alta_plantilla.html", {'formulario': reservas_form, 'tipoalta': 'Reservas', 'vinculo': 'reservas'})
