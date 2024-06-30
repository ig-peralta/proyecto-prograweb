from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Categoria, Producto, Perfil

# *********************************************************************************************************#
#                                                                                                          #
# INSTRUCCIONES PARA EL ALUMNO, PUEDES SEGUIR EL VIDEO TUTORIAL, COMPLETAR EL CODIGO E INCORPORAR EL TUYO: #
#                                                                                                          #
# https://drive.google.com/drive/folders/1ObwMnpKmCXVbq3SMwJKlSRE0PCn0buk8?usp=drive_link                  #
#                                                                                                          #
# *********************************************************************************************************#

# PARA LA PAGINA MANTENEDOR DE PRODUCTOS:
# Crea ProductoForm como una clase que hereda de ModelForm
# asocialo con el modelo Producto
# muestra todos los campos
# crea 2 widgets para:
#   - la descripción del producto como TextArea
#   - el botón de cargar imagen como FileInput y 
#     escóndelo para reemplazarlo por otro acorde 
#     con tu diseño gráfico
# renombra las siguientes etiquetas para que ocupen menos
# espacio en la página: 'Nombre', 'Subscriptor(%)' y 'Oferta(%)'
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class BodegaForm(Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoría')
    producto = forms.ModelChoiceField(queryset=Producto.objects.none(), label='Producto')
    cantidad = forms.IntegerField(label='Cantidad')
    class Meta:
        fields = '__all__'

class IngresarForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Cuenta")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']

class RegistroUsuarioForm(UserCreationForm):
   class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2',
            ]
        labels = {
            'username' : 'Usuario',
            'email' : 'Correo',
            'password2' : 'Confirmar contraseña'
        }

class RegistroPerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'rut',
            'direccion',
            'subscrito',
            'imagen',
        ]
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'imagen' : forms.FileInput()
        }
        
    def __init__(self, *args, **kwargs):
        super(RegistroPerfilForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False

class UsuarioForm(ModelForm):
   class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]
        labels = {
            'username' : 'Usuario',
            'email' : 'Correo',
            'password2' : 'Confirmar contraseña'
        }

class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'tipo_usuario',
            'rut',
            'direccion',
            'subscrito',
            'imagen'
        ]
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'imagen' : forms.FileInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False