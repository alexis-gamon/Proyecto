from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    Nombre = models.CharField(max_length = 30)# si se necesitan mas campos los puedes agregar y dar de alta en el forms.py
    Edad = models.PositiveIntegerField(null = True, blank = True)
    Pais = models.CharField(max_length = 30)



