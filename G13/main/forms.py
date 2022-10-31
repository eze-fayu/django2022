from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre:", required=False, max_length=50)
    apellido = forms.CharField(label="Apellido de contacto", required=False, max_length=50)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea(attrs={"rows":"5", "label":"Apellido de contacto", "required":"True"}))
