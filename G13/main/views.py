from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

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

            template = render_to_string('main/email_template.html', {
                'nombre': nombre,
                'apellido': apellido,
                'email': email,
                'mensaje': mensaje
            })

            email = EmailMessage(
                "Mensaje desde la web", 
                template, 
                settings.EMAIL_HOST_USER,
                ['xxxxx@gmail.com'], # correo desde donde se envia
                reply_to=[email]
            )

            email.fail_silently = False
            email.send()

            messages.success(request, "Mensaje enviado correctamente")

            return redirect('contacto')
    else:
        contacto_form = ContactoForm()
    return render(request, "main/contacto.html", {'contacto_form': contacto_form})

def registro(request):
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado correctamente')
            # register_form = UserCreationForm()
            return redirect('catalogo')
    else:
        register_form = UserCreationForm()
    return render(request, "register.html", {'register_form': register_form})