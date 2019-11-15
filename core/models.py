from django.db import models
from django.utils import timezone
# Create your models here.

class Cliente(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    rut = models.CharField(max_length=100, blank=False, null=False)
    telefono = models.IntegerField(blank=False, null=False)
    correo = models.EmailField( max_length=254)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Casa(models.Model):

    opciones = [
    ('Venta', 'Venta'),
    ('Arriendo', 'Arriendo')
    ]

    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='Casas')
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=19, decimal_places=0)
    cant_habitaciones = models.IntegerField(blank=False, null=False)
    cant_baños = models.IntegerField(blank=False, null=False)
    metros_2 = models.DecimalField(max_digits=19, decimal_places=0)
    patio = models.BooleanField()
    tipo_contacto = models.CharField(max_length=10, choices=opciones)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True,default=timezone.now)
    destacado = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "Casa"
        verbose_name_plural = "Casas"
        ordering = ['-created_date']
        
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Departamento(models.Model):

    opciones = [
    ('Venta', 'Venta'),
    ('Arriendo', 'Arriendo')
    ]

    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='Departamentos')
    direccion = models.CharField(max_length=200)
    num_piso = models.IntegerField(max_length=2, blank=False, null=False)
    ciudad = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=19, decimal_places=0)
    cant_habitaciones = models.IntegerField(blank=False, null=False)
    cant_baños = models.IntegerField(blank=False, null=False)
    metros_2 = models.DecimalField(max_digits=19, decimal_places=0)
    tipo_contacto = models.CharField(max_length=10, choices=opciones)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True,default=timezone.now)
    destacado = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['-created_date']
        
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Terreno(models.Model):

    opciones = [
    ('Venta', 'Venta'),
    ('Arriendo', 'Arriendo')
    ]

    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='Terrenos')
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=19, decimal_places=0)
    metros_2 = models.DecimalField(max_digits=19, decimal_places=0)
    tipo_contacto = models.CharField(max_length=10, choices=opciones)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True,default=timezone.now)
    destacado = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "Terreno"
        verbose_name_plural = "Terrenos"
        ordering = ['-created_date']
        
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Galeria(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)  
    imagen = models.ImageField(upload_to='Galeria')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True,default=timezone.now)

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerias"
        ordering = ['-created_date']
        
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

