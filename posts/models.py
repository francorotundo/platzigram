"""Posts models."""

# Django
from django.db import models
# from django.forms import DateTimeField

# class User(models.Model):
#     """User model."""

#     email = models.EmailField(unique=True) #unique para que el email sea unico en la base de datos
#     password = models.CharField(max_length=100) #max length para definir el numero maximo de caracteres

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)

#     is_admin = models.BooleanField(default=False)

#     bio = models.TextField(blank=True) #blank para pueda estar sin informacion el bio

#     birthdate = models.DateField(blank=True, null=True) #en caso de fechas de nacimiento si no se coloca el valor va a ser null

#     created = models.DateTimeField(auto_now_add=True) #auto_now_add va a colocar la fecha en la que se crea el ususario
#     modified = models.DateTimeField(auto_now=True) #auto_now va a actualizar la fecha cada ves que se realice una modificación al usuario

