from django.shortcuts import render, redirect
from .forms import ContactoForm
# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def contacto(request):
    if request.method == "POST":
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            # request.post es un diccionario que tiene :
            # <QueryDict: {'csrfmiddlewaretoken': ['8359bj78AaLzCqUP7Ubk541YhDteAlIG87S6WnamkkzbJA9PK39gVid3sl8pxPSX'], 'nombre': ['casillacon'], 'apellido': ['casilape'], 'email': ['main@mail.com'], 'mensaje': ['mensaje_enviado']}>
            nombre = contacto_form.cleaned_data['nombre']
            apellido = contacto_form.cleaned_data['apellido']
            email = contacto_form.cleaned_data['email']
            mensaje = contacto_form.cleaned_data['mensaje']
        
    else:
        contacto_form = ContactoForm()
    return render(request, "main/contacto.html", {'contacto_form': contacto_form})

