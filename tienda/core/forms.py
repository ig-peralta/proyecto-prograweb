from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Categoria, Producto, Bodega, Perfil

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'descripcion' : forms.Textarea(),
            'imagen' : forms.FileInput(attrs={'class' : 'none'})
        }
        labels = {
            'nombre' : 'Nombre',
            'descuento_subscriptor' : 'Subscriptor(%)',
            'descuento_oferta' : 'Oferta(%)'
        }

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class BodegaForm(ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'

class Perfil(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'

class RegistrarmeForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',]

class IngresarForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), label='Cuenta')
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    class Meta:
        fields = ['username', 'password']