from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    context = {
        'productos' : productos
    }
    return render(request, 'index.html', context)

def ficha(request, producto_id):
    producto = Producto.objects.filter(id=producto_id).get()
    context = {
        'producto' : producto
    }
    return render(request, 'ficha.html', context)