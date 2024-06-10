from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart
from .forms import BlankForm, BookletForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from django.views.generic import DetailView
# from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def shop(request):
    return render(request, 'shop/shop.html')

def thankyou(request):
    return render(request, 'shop/thankyou.html')

def prices(request):
    products = Product.objects.all()
    return render(request, 'shop/prices.html', {'products': products})

def contact(request):
    return render(request, 'shop/contact.html')
@login_required
def blank(request):
    if request.method == 'POST':
        form = BlankForm(request.POST, request.FILES)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.user = request.user
            cart.save()
            return redirect('/cart')  
    else:
        form = BlankForm()
    return render(request, 'shop/blank.html', {'form': form})

@login_required
def booklet(request):
    if request.method == 'POST':
        form = BlankForm(request.POST, request.FILES)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.user = request.user
            cart.save()
            return redirect('/cart')  
    else:
        form = BookletForm()
    return render(request, 'shop/booklet.html', {'form': form})

@login_required
def flyer(request):
    if request.method == 'POST':
        form = BlankForm(request.POST, request.FILES)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.user = request.user
            cart.save()
            return redirect('/cart')  
    else:
        form = BookletForm()
    return render(request, 'shop/flyer.html', {'form': form})

@login_required
def poster(request):
    if request.method == 'POST':
        form = BlankForm(request.POST, request.FILES)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.user = request.user
            cart.save()
            return redirect('/cart')  
    else:
        form = BookletForm()
    return render(request, 'shop/poster.html', {'form': form})

@login_required
def leaflet(request):
    if request.method == 'POST':
        form = BlankForm(request.POST, request.FILES)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.user = request.user
            cart.save()
            return redirect('/cart')  
    else:
        form = BookletForm()
    return render(request, 'shop/leaflet.html', {'form': form})

def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'shop/cart.html', {'cart_items': cart_items})

def cart_item_delete(request, id):
    if request.method == "POST":
        item = Cart.objects.get(id=id)
        item.delete()