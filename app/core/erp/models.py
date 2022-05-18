from django.db import models
from datetime import datetime

# Create your models here.


class Type (models.Model):
    name = models.CharField(max_length=150,verbose_name='Nombre')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        ordering=['-id']

class Category(models.Model):
    name = models.CharField(max_length=150,verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        ordering = ['-id']



class Employee(models.Model):
    categoria = models.ManyToManyField(Category)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    names = models.CharField(max_length=150,verbose_name='Nombres')
    dni = models.CharField(max_length=9,unique=True,verbose_name='dni')
    entrada = models.DateField(default=datetime.now,verbose_name='Fecha de registro')
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    edad = models.IntegerField(default=0)
    genero = models.CharField(max_length=50)
    #edad = models.PositiveIntegerField(default=0)
    salario = models.DecimalField(max_digits=9,decimal_places=2)
    estado = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/d',null=True,blank=True)
    cv = models.FileField(upload_to='cvitae/%Y/%m/d',null=True,blank=True)
    def __str__(self):
        return self.names
    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        db_table='empleado'
        ordering=['-id']



