from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Autores_Form, Usuarios_Form, Libros_Form, Ejemplares_Form, Prestamos_Form, Devoluciones_Form, Reservas_Form
from .models import autores, ejemplares
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def index_catalogo(request):
    return render(request, "catalogo/index.html")

@login_required(login_url='/login')    
def alta_autores(request):

    if request.method == "POST":
        autores_form = Autores_Form(request.POST)  # instance=autores es para usarlo como editor
        if autores_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            autores_form.nombre = autores_form.cleaned_data['nombre'].capitalize()
            autores_form.apellido = autores_form.cleaned_data['apellido'].capitalize()
            autores_form.nacionalidad = autores_form.cleaned_data['nacionalidad'].capitalize()
            autores_form.save()
            messages.success(request, "Autor Registrado correctamente")
            autores_form = Autores_Form()
            return render(request, "catalogo/alta_plantilla.html", {'formulario': autores_form, 'tipoalta': 'Autor', 'vinculo': 'autores_alta'})
    else:
        autores_form = Autores_Form()
        return render(request, "catalogo/alta_plantilla.html", {'formulario': autores_form, 'tipoalta': 'Autor', 'vinculo': 'autores_alta'})

@login_required(login_url='/login')
def alta_usuarios(request):

    if request.method == "POST":
        usuarios_form = Usuarios_Form(request.POST)
        if usuarios_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            usuarios_form.nombre = usuarios_form.cleaned_data['nombre'].capitalize()
            usuarios_form.apellido = usuarios_form.cleaned_data['apellido'].capitalize()
            usuarios_form.save()
            usuarios_form = Usuarios_Form()
            messages.success(request, "Usuario Registrado correctamente")

            return render(request, "catalogo/alta_plantilla.html", {'formulario': usuarios_form, 'tipoalta': 'Usuario', 'vinculo': 'alta_usuario'})
    else:
        usuarios_form = Usuarios_Form()
        return render(request, "catalogo/alta_plantilla.html", {'formulario': usuarios_form, 'tipoalta': 'Usuario', 'vinculo': 'alta_usuario'})

@login_required(login_url='/login')
def alta_libros(request):

    if request.method == "POST":
        libros_form = Libros_Form(request.POST)
        if libros_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            libros_form.save()
            libros_form = Libros_Form()
            messages.success(request, "Autor Registrado correctamente")

            return render(request, "catalogo/alta_plantilla.html", {'formulario': libros_form, 'tipoalta': 'Libros', 'vinculo': 'alta_libros'})
    else:
        libros_form = Libros_Form()
        return render(request, "catalogo/alta_plantilla.html", {'formulario': libros_form, 'tipoalta': 'Libros', 'vinculo': 'alta_libros'})

@login_required(login_url='/login')
def alta_ejemplares(request):

    if request.method == "POST":
        ejemplares_form = Ejemplares_Form(request.POST)
        if ejemplares_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            ejemplares_form.save()
            ejemplares_form = Ejemplares_Form()
            messages.success(request, "Autor Registrado correctamente")

            return render(request, "catalogo/alta_plantilla.html", {'formulario': ejemplares_form, 'tipoalta': 'Ejemplares', 'vinculo': 'alta_ejemplares'})
    else:
       ejemplares_form = Ejemplares_Form()
       return render(request, "catalogo/alta_plantilla.html", {'formulario': ejemplares_form, 'tipoalta': 'Ejemplaress', 'vinculo': 'alta_ejemplares'})

@login_required(login_url='/login')
def prestamos(request):

    if request.method == "POST":
        prestamo_form = Prestamos_Form(request.POST)
        if prestamo_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            prestamo_form.save()
            prestamo_form = Prestamos_Form()
            messages.success(request, "Autor Registrado correctamente")

            return render(request, "catalogo/alta_plantilla.html", {'formulario': prestamo_form, 'tipoalta': 'Prestamos', 'vinculo': 'prestamos'})
    else:
        prestamo_form = Prestamos_Form()
        return render(request, "catalogo/alta_plantilla.html", {'formulario': prestamo_form, 'tipoalta': 'Prestamos', 'vinculo': 'prestamos'})

@login_required(login_url='/login')
def devoluciones(request):

    if request.method == "POST":
        devoluciones_form = Devoluciones_Form(request.POST)
        if devoluciones_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            devoluciones_form.save()
            devoluciones_form = Devoluciones_Form()
            messages.success(request, "Autor Registrado correctamente")

            return render(request, "catalogo/alta_plantilla.html", {'formulario': devoluciones_form, 'tipoalta': 'Devoluciones', 'vinculo': 'devoluciones'})
    else:
        devoluciones_form = Devoluciones_Form()
        return render(request, "catalogo/alta_plantilla.html", {'formulario': devoluciones_form, 'tipoalta': 'Devoluciones', 'vinculo': 'devoluciones'})

@login_required(login_url='/login')
def reservas(request):

    if request.method == "POST":
        reservas_form = Reservas_Form(request.POST)
        if reservas_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            reservas_form.save()
            reservas_form = Reservas_Form()
            messages.success(request, "Autor Registrado correctamente")

            return render(request, "catalogo/alta_plantilla.html", {'formulario': reservas_form, 'tipoalta': 'Reservas', 'vinculo': 'reservas'})
    else:
        reservas_form = Reservas_Form()
        return render(request, "catalogo/alta_plantilla.html", {'formulario': reservas_form, 'tipoalta': 'Reservas', 'vinculo': 'reservas'})

@login_required(login_url='/login')
def consultas(request, apellido ):
    apellido = apellido.capitalize()
    autores_busqueda = autores.objects.filter(apellido=apellido)
    print(autores_busqueda)
    if autores_busqueda is not None:
        return render(request, "catalogo/index.html", {'autores': autores_busqueda})
    else:
        return render(request, "catalogo/index.html")

@login_required(login_url='/login')
def catalogo(request ):
    catalogo_gral = ejemplares.objects.all()
    if catalogo_gral is not None:
        return render(request, "catalogo/index.html", {'ejemplares': catalogo_gral})
    else:
        return render(request, "catalogo/index.html")