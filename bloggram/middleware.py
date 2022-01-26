"""Debo instalar este Middleware en Settings"""

# Django
from urllib import response
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Insure every user that is interacting with the platform
    have their profile picture and biography"""

    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request befor the view is called"""
        # debemos asegurarnos que haya un usuario logueado
        if not request.user.is_anonymous:
            # traemos el perfil
            if not request.user.is_staff: # este if es para que pueda entrar como admin y no me pida actualizar profile
                profile = request.user.profile
                # validamos
                if not profile.picture or not profile.biography:
                    # si el path no está en estas dos url
                    if request.path not in [reverse('users:update'), reverse('users:logout')]: # debo importar reverse para poder traer el nombre de la url
                        return redirect ('users:update')

        response = self.get_response(request)
        return response