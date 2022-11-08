from django.db import models

# Create your models here.

class Informacion(models.Model):
    opciones_categoria = (('1', 'Alimentos'), ('2', 'Bebidas'), ('3', 'Limpieza'), ('4', 'Otros'))
    opciones_unidades = (('1', 'Kg'), ('2', 'g'), ('3', 'L'), ('4', 'Unidades'), ('5', 'Otros'))
    #como se vera el modelo en la página
    class Meta:
        verbose_name_plural = 'Información'
    #elementos de la base de datos
    id = models.AutoField(primary_key=True)
    nombre_descripcion = models.CharField(max_length = 255, verbose_name="Nombre y descripción")
    proveedor =  models.CharField(max_length = 255, verbose_name="Proveedor")
    direccion_proveedor =  models.CharField(max_length = 255, verbose_name="Dirección del proveedor")
    numero_proveedor =  models.CharField(max_length = 255, verbose_name="Número del contacto del proveedor")
    fecha_modificacion =  models.DateField(max_length = 20,verbose_name = "Fecha de modificación")
    fecha_vencimiento =  models.DateField(max_length = 20,verbose_name="Fecha de vencimiento")
    categoria_producto = models.CharField(max_length = 100, verbose_name="Categoria del producto", choices = opciones_categoria)
    cantidad_productos = models.IntegerField(verbose_name="Cantidad actual")
    stock_maximo = models.IntegerField(verbose_name="Stock minima")
    peso_unidad = models.FloatField(verbose_name="Peso por unidad")
    stock_minimo = models.IntegerField(verbose_name="Stock maxima")
    unidades = models.CharField(max_length = 255, choices = opciones_unidades, verbose_name="Unidades")
    #El nombre para reflejarlo en la página, en este caso que muestre el nombre y descripción
    def __str__(self):
        return self.nombre_descripcion
