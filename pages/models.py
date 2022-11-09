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

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('pelicula_detalle', args=(str(self.id)))

   
