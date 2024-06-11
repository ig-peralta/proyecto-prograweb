from django.shortcuts import render, redirect
from .models import Producto
from .forms import IngresarForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def index(request):
    user = request.user
    productos = Producto.objects.all()
    context = {
        'user' : user,
        'productos' : productos
    }
    return render(request, 'index.html', context)

def ficha(request, producto_id):
    user = request.user
    producto_ficha = Producto.objects.filter(id=producto_id).get()
    productos = Producto.objects.all()
    context = {
        'user' : user,
        'producto_ficha' : producto_ficha,
        'productos' : productos
    }
    return render(request, 'ficha.html', context)

def nosotros(request):
    user = request.user
    context = {
        'user' : user,
    }
    return render(request, 'nosotros.html', context)

def premio(request):
    user = request.user
    context = {
        'user' : user,
    }
    return render(request, 'premio.html', context)

@csrf_protect
def ingresar(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = IngresarForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request, 
                username = username, 
                password = password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = IngresarForm()
        context = {
            'form_ingresar' : form
        }
    return render(request, 'ingresar.html', context)

def salir(request):
    logout(request)
    return redirect('index')

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('login')
#     else:
#         form = SignupForm()
#         context = {
#             'form' : form
#         }
#     return render(request, 'signup.html', context)