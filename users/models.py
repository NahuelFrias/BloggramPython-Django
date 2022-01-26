from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Proxy model extiende de auth.user
    User ya viene con distintos campos como username, lastname, id o email
    en Profile agregamos algunos campos como website o biography"""
    user = models.OneToOneField(User, on_delete=models.CASCADE) # se borra en cascada

    website = models.URLField(max_length=200, blank=True) # URLfield agrega validaciones
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True) # folder de la imagen 'user/pictures'

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
