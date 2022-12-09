from django.db import models
from django import forms

# Create your models here.
class autores(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    nacionalidad = models.CharField(max_length=50, verbose_name="Nacionalidad")
    def __str__(self):
        return self.nombre + " " + self.apellido

class libros(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Titulo")
    autor = models.ForeignKey(autores, on_delete=models.CASCADE)
    editorial = models.CharField(max_length=50, verbose_name="Editorial")
    def __str__(self):
        return self.titulo + " " + self.editorial

class ejemplares(models.Model):
    libro = models.ForeignKey(libros, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, verbose_name="Edición")
    def __str__(self):
        return self.libro.titulo + " - " + self.libro.autor.nombre + " - " + self.libro.autor.apellido + " - " + self.libro.editorial + " - " + self.estado

class usuarios(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    dni = models.CharField(max_length=50, verbose_name="DNI")
    domicilio = models.CharField(max_length=50, verbose_name="Domicilio")
    telefono = models.CharField(max_length=50, verbose_name="Telefono")
    def __str__(self):
        return self.nombre + " " + self.apellido

class prestamos(models.Model):
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    ejemplar = models.ForeignKey(ejemplares, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    def __str__(self):
        return str(self.fecha_prestamo) +  " - " + self.usuario.nombre + " " + self.usuario.apellido + " - " + self.ejemplar.libro.titulo

class devoluciones(models.Model):
    prestamo = models.ForeignKey(prestamos, on_delete=models.CASCADE)
    fecha_devolucion_prestamo = models.DateField()
    def __str__(self):
        return self.fecha_devolucion_prestamo

class reservas(models.Model):
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    ejemplar = models.ForeignKey(ejemplares, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    fecha_devolucion = models.DateField()
    def __str__(self):
        return self.fecha_reserva

