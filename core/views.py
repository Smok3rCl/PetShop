from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import time
from rest_framework import viewsets
from .serializers import *
import requests


# CREANDO UNA CLASE QUE VA A PERMITIR LA TRANSFORMACIÓN
class ProductoViewset(viewsets.ModelViewSet):
     queryset = Producto.objects.all()
     serializer_class = ProductoSerializers

class TipoProductoViewset(viewsets.ModelViewSet):
     queryset = TipoProducto.objects.all()
     serializer_class = TipoProductoSerializers


def index(request):
	return render(request, 'core/index.html')


def about(request):
	return render(request, 'core/about.html')

@login_required
def cart(request):
    respuesta2 = requests.get('https://mindicador.cl/api/dolar')
    monedas = respuesta2.json()
    valor_usd = monedas['serie'][0]['valor']
    valor_carrito = 20000
    total = valor_carrito / valor_usd

    data = {
         'valor' : round(total, 2),
    }

    return render(request, 'core/cart.html', data)

@login_required
def checkout(request):
	return render(request, 'core/checkout.html')

def contact_us(request):
	return render(request, 'core/contact-us.html')

@login_required
def my_account(request):
	return render(request, 'core/my-account.html')


@login_required
def shop(request):
    productos = Producto.objects.all()

    paginator = Paginator(productos, 3)  # Especifica cuántos elementos quieres mostrar por página

    page = request.GET.get('page', 1)
    productos = paginator.get_page(page)

    data = {
        'listado': productos,
        'paginator': paginator
    }

    return render(request, 'core/shop.html', data)

@login_required
def shopapi(request):
    respuesta = requests.get('http://127.0.0.1:8000/api/productos/')
    respuesta2 = requests.get('https://mindicador.cl/api/')
    respuesta3 = requests.get('https://rickandmortyapi.com/api/character')


    datita = respuesta.json()
    datita2 = respuesta2.json()
    aux = respuesta3.json()
    personajes = aux['results']

    data = {
        'listado': datita,
        'moneda' : datita2,
        'personajes' : personajes,
    }

    return render(request, 'core/shopapi.html', data)


@login_required
def seguimiento(request):
	return render(request, 'core/seguimiento.html')

@login_required
def mapa(request):
	return render(request, 'core/mapa.html')

@login_required
def suscripcion(request):
    return render(request, 'core/suscripcion.html')


#CRUD
def add(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save() 
            data['msj'] = "Producto almacenado correctamente"
            messages.success(request, "Producto almacenado correctamente")

    return render(request, 'core/add-product.html', data)


def update(request,id):
    producto = Producto.objects.get(id=id) 
    data = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':

        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save() 
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario
	     

    return render(request, 'core/update-product.html', data)

    

def delete(request,id):
    producto = Producto.objects.get(id=id) 
    producto.delete()

    return redirect(to="shop")


def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'shop.html', {'productos': productos})

def agregar_al_carrito(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            cantidad = formulario.cleaned_data['cantidad']
            carrito = request.session.get('carrito', [])
            carrito.append({'producto': producto, 'cantidad': cantidad})
            request.session['carrito'] = carrito
            return redirect(to="cart")

    formulario = ProductoForm()
    return render(request, 'agregar_al_carrito.html', {'producto': producto, 'formulario': formulario})

def ver_carrito(request):
    carrito = request.session.get('carrito', [])
    return render(request, 'cart.html', {'carrito': carrito})



