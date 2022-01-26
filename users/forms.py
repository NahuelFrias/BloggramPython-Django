"""user forms"""

# Django
from xml.dom import ValidationErr
from django import forms
# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    # por default si no ponemos required es True
    username = forms.CharField(min_length=4, max_length=50)

    # widget: representacion de Django de html (inputs, values, etc)
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    # widget necesario para tratarlo como email
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    # validamos que el username no este en uso
    def clean_username(self):
        # hacemos una query y tramos el valor
        self.cleand_data['username']
        # esto regresa un booleano si existe el user
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            # lanzamos la exc
            raise forms.ValidationError('Username is already in use.')
        return username  # siempre que hagamos la validacion debemos regresar el datos

    # validamos password confirmation
    def clean(self):
        # traemos los datos de clean con super
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password do not match.')
        return data

    # salvamos
    def save(self):
        data = self.cleaned_data
        # quitamos password_confirmation porque no nos sirve
        data.pop('password_confirmation')

        # mandamos todo el diccionario con los datos con **
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.ModelForm):
    website = forms.URLField(max_length=200, required=False)
    biography = forms.CharField(max_length=500, required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField(required=True)

    class Meta:
        model = Profile
        fields = ['website', 'biography', 'phone_number', 'picture'] # campos que editamos en la vista de users
