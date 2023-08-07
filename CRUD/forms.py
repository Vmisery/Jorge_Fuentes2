from django.forms import ModelForm, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario


class CustomUserRegister(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder:':'Ingresa Nombre de usuario'}))
    email = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder:':'Ingresa email'}))
    password1 = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder:':'Ingresa contraseña'}))
    password2 = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder:':'Ingresa contraseña nuevamente'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
                account = Usuario.objects.exclude(pk=self.instance.pk).get(email=email)
        except Usuario.DoesNotExist:
                return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Usuario.objects.exclude(pk=self.instance.pk).get(username=username)
        except Usuario.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)
    
class SearchForm(forms.Form):
    search_query = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Buscar'}))