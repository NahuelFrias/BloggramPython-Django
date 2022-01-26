# Django
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

"""Tu ve que deletear el archivo de migraciones 0001
Hacer el makemigrations
Cambiar el nombre a: 0001_initial_manual.py
Hace migrate nombreApp (en este caso posts)
Asi pude crear la tabla en la BD"""

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=CASCADE) # relaciono con User
    profile = models.ForeignKey('users.Profile', on_delete=CASCADE) # relaciono con Profile
    # usar el string es igual de valido para no importar

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos') # donde queremos que guarde la foto

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return f'{self.title} by @{self.user.username}'