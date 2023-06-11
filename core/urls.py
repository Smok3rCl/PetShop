from django.urls import path, include
from .views import *
from rest_framework import routers

# CREAMOS LAS RUTAS PARA LA API
router = routers.DefaultRouter()
router.register('productos', ProductoViewset)
router.register('tipoproductos', TipoProductoViewset)


urlpatterns = [
    # API
    path('api/', include(router.urls)),

    path('', index, name="index"),
	path('about/',about, name="about"),
    path('cart/',cart, name="cart"),
    path('checkout/',checkout, name="checkout"),
    path('contact-us/',contact_us, name="contact-us"),
	path('my-account/',my_account, name="my-account"),
    path('shop/',shop, name="shop"),
    path('shopapi/',shopapi, name="shopapi"),
    path('seguimiento/',seguimiento, name="seguimiento"),
    path('mapa/',mapa, name="mapa"),
    path('suscripcion/', suscripcion, name="suscripcion"),
    path('productos/', ver_productos, name='ver_productos'),

   #CRUD
    path('add/', add, name="add"),
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),
]	


