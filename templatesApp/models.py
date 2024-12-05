from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imgproduct/', blank=True, null=True)
    detalle = models.TextField(max_length=1000, verbose_name='Información del producto')
    precio = models.FloatField()
    marca = models.CharField(max_length=20)
    disponible = models.BooleanField(default=True)
    habilitado = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)


    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Usuario(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=12)
    

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['rut']

