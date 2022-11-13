from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Autores_Form, Usuarios_Form

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

            return redirect('alta_autores')
    else:
        autores_form = Autores_Form()
    return render(request, "catalogo/autores_alta.html", {'autores': autores_form})


def alta_usuarios(request):

    if request.method == "POST":
        usuarios_form = Usuarios_Form(request.POST)
        if usuarios_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            usuarios_form.save()

            messages.success(request, "Autor Registrado correctamente")

            return redirect('alta_autores')
    else:
        usuarios_form = Usuarios_Form()
    return render(request, "catalogo/alta_plantilla.html", {'formulario': usuarios_form, 'tipoalta': 'Usuario'})