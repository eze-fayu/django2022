from django.shortcuts import render, redirect
from .forms import ContactoForm

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def contacto(request):
    if request.method == "POST":
        contacto_form = ContactoForm(request.POST)
        contacto_form.is_valid()
        
        
    else:
        contacto_form = ContactoForm()
    return render(request, "main/contacto.html", {'contacto_form': contacto_form})

