from django.urls import path
from .views import index, ficha
# from .views import index, registrarme, nosotros, admin_productos
# from .views import admin_usuarios, admin_bodega, ventas, boleta, ingresar, admin_usuarios
# from .views import misdatos, miscompras, salir, carrito, ficha
# from .views import cambiar_estado_boleta, poblar, obtener_productos, eliminar_producto_en_bodega
# from .views import premio, eliminar_producto_en_carrito, agregar_producto_al_carrito
# from .views import vaciar_carrito, mipassword, cambiar_password

urlpatterns = [
    path('', index, name='index'),
    # path('registrarme', registrarme, name='registrarme'),
    # path('nosotros', nosotros, name='nosotros'),
    # path('admin_productos/<accion>/<id>', admin_productos, name='admin_productos'),
    # path('admin_usuarios/<accion>/<id>', admin_usuarios, name='admin_usuarios'),
    # path('cambiar_password', cambiar_password, name='cambiar_password'),
    # path('admin_bodega', admin_bodega, name='admin_bodega'),
    # path('obtener_productos', obtener_productos, name='obtener_productos'),
    # path('eliminar_producto_en_bodega/<bodega_id>', eliminar_producto_en_bodega, name='eliminar_producto_en_bodega'),
    # path('ventas', ventas, name='ventas'),
    # path('boleta/<nro_boleta>', boleta, name='boleta'),
    # path('cambiar_estado_boleta/<nro_boleta>/<estado>', cambiar_estado_boleta, name='cambiar_estado_boleta'),
    # path('ingresar', ingresar, name='ingresar'),
    # path('misdatos', misdatos, name='misdatos'),
    # path('mipassword', mipassword, name='mipassword'),
    # path('miscompras', miscompras, name='miscompras'),
    # path('salir', salir, name='salir'),
    # path('carrito', carrito, name='carrito'),
    # path('eliminar_producto_en_carrito/<carrito_id>', eliminar_producto_en_carrito, name='eliminar_producto_en_carrito'),
    # path('vaciar_carrito', vaciar_carrito, name='vaciar_carrito'),
    # path('agregar_producto_al_carrito/<producto_id>', agregar_producto_al_carrito, name='agregar_producto_al_carrito'),
    path('ficha/<producto_id>', ficha, name='ficha'),
    # path('premio', premio, name='premio'),
    # path('poblar', poblar, name='poblar'),
]