from django import forms
from .models import autores, libros, ejemplares, usuarios, prestamos, devoluciones, reservas


class Autores_Form(forms.ModelForm):
    class Meta:
        model = autores
        fields = '__all__'

class Libros_Form(forms.ModelForm):
    class Meta:
        model = libros
        fields = '__all__'

class Ejemplares_Form(forms.ModelForm):

    class Meta:
        model = ejemplares
        fields = '__all__'

class Usuarios_Form(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = '__all__'

class Prestamos_Form(forms.ModelForm):
    class Meta:
        model = prestamos
        fields = '__all__'

class Devoluciones_Form(forms.ModelForm):
    class Meta:
        model = devoluciones
        fields = '__all__'

class Reservas_Form(forms.ModelForm):
    class Meta:
        model = reservas
        fields = '__all__'

