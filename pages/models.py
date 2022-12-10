from secrets import choice
from django.db import models
from django.contrib.auth import get_user_model

from django.urls import reverse


class Pelicula(models.Model):
    Nombre = models.CharField(max_length=30)

    Descripcion = models.TextField(max_length=250)


    Creador = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    AñoLanzamiento = models.PositiveIntegerField(null = True, blank = True)

    
    Duracion = models.PositiveIntegerField(null = True, blank = True)

    Fecha = models.DateTimeField(auto_now_add=True)

    Precio = models.PositiveIntegerField(null = True, blank = True)

    portada = models.ImageField(upload_to = 'portada/', blank = True)#esto es unicamente para imagenes 


    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('pelicula_detalle', args=(str(self.id)))

    class Meta:
        permissions = [
            ('admin_generic', 'Puede Editar y Crear Peliculas'),
            ('suscriptor', 'Solo mostrara el detalle')
        ]


class Cine(models.Model):
    Nombre = models.CharField(max_length=30)

    Ubicacion = models.TextField(max_length=50)

    pelicula = models.ForeignKey(Pelicula, on_delete = models.CASCADE)
   
    Epson = 'Epson'
    Canon = 'Canon'
    Generic = 'Generic'

    TiposProyector = [
        (Epson,'Epson'),
        (Canon,'Canon'),
        (Generic,'Generic'),

    ]

    Proyector = models.CharField(max_length=10, choices=TiposProyector, default = 'Epson')








   
