from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True)
    detalle = models.TextField(max_length=1000, verbose_name='Información del producto')
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)
    

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
