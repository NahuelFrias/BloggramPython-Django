# Django
from django.urls import reverse, reverse_lazy #construye urls
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import views as auth_views

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# Forms
from users.forms import ProfileForm, SignupForm

"""autenticamos el inicio de sesion para entrar en esta vista"""

# esta clase me ayuda a traer el user en el url
class UserDetailView(LoginRequiredMixin, DetailView):

    template_name='users/detail.html'
    slug_field = 'username' # este slug es el que enviamos a la url para llamar al username
    slug_url_kwarg = 'username'
    queryset=User.objects.all()

    # esta funcion es para traer los posts del usuario
    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    # siempre que usemos un FormView debemos sobreescribir el form_valid
    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form) # redireccionamos

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    form_class = ProfileForm

    def get_object(self): # regresa el perfil del usuario
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self): # trae el username
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

class LoginView(auth_views.LoginView):
    """Login view. Solo debemos pasar el html y Django hace toda la magia"""
    redirect_authenticated_user = True
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view. No hace falta pasar un template, solo configuramos el setting"""
    pass
