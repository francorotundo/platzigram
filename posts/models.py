"""Posts models."""

# Django
from django.db import models
from django.forms import DateTimeField
from django.contrib.auth.models import User
#from users.models import Profile

class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title =  models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photo')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username"""

        return '{} by @{}'.format(self.title, self.user.username)


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

