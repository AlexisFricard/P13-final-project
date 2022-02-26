"""
FORMS SETTINGS
"""
from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('image', 'title')


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='Prenom', max_length=50)
    last_name = forms.CharField(label='Nom', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(
        label='Mot de passe',
        max_length=50,
        widget=forms.PasswordInput()
        )


class ActualityForm(forms.Form):
    title = forms.CharField(max_length=200)
    date = forms.DateField()
    stop_date = forms.DateField()
    article = forms.CharField()
    link = forms.CharField(max_length=400)
