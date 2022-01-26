# Django
from django import forms
# Models
from posts.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # fields o campos que usaremos del modelo Post
        fields = ('user', 'profile', 'title', 'photo')