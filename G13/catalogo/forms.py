from django import forms
from .models import autores, libros, ejemplares, usuarios, prestamos, devoluciones, reservas, multas, pagos


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

class prestamos_form(forms.ModelForm):
    class Meta:
        model = prestamos
        fields = '__all__'

class devoluciones_form(forms.ModelForm):
    class Meta:
        model = devoluciones
        fields = '__all__'

class reservas_form(forms.ModelForm):
    class Meta:
        model = reservas
        fields = '__all__'

class multas_form(forms.ModelForm):
    class Meta:
        model = multas
        fields = '__all__'

class pagos_form(forms.ModelForm):
    class Meta:
        model = pagos
        fields = '__all__'
