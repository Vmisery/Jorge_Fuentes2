from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from .models import *
from .forms import CustomUserRegister
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, 'home.html', context)

def mision(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, '2.html', context)

def galeria(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, '3.html', context)

def galeriap(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, '3.html', context)

def formulario(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, '4.html', context)

def mapa(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, '5.html', context)

def galeria1(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, 'galeria/1.html', context)

def galeria2(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, 'galeria/2.html', context)

def galeria3(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, 'galeria/3.html', context)

def galeria4(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, 'galeria/4.html', context)

def galeria5(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, 'galeria/5.html', context)

def galeria6(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, 'galeria/6.html', context)

def galeria7(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, 'galeria/7.html', context)

def galeria8(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, 'galeria/8.html', context)

def galeria9(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, 'galeria/9.html', context)


@login_required
def cart(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, 'store/cart.html', context)



def checkout(request):
    cart = carrito.objects.get(id='666')
    cart_items = cart.productocarrito_set.all()
    obras = obra.objects.all()
    context = {'cart': cart, 'cart_items': cart_items, 'obras': obras}
    return render(request, 'store/checkout.html', context)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
        'form': CustomUserRegister()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = Usuario.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                 return render(request, 'signup.html', {
                    'form': CustomUserRegister(),
                    'error': 'El usuario ya existe'
                })

        return render(request, 'signup.html', {
            'form': CustomUserRegister(),
            'error': 'Las contraseñas no coinciden'
        })

def gestionobras(request):
    return render(request, 'gestionobras.html')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'El usuario o la contraseña son incorrectos'})
        else:
            login(request, user)
            return redirect('/')