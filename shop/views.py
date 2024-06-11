from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, Notification, Support, Order
from .forms import BlankForm, BookletForm, FlyerForm, PosterForm, LeafletForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from django.views.generic import DetailView
from django.http import HttpResponseRedirect

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
        form = BookletForm(request.POST, request.FILES)
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
        form = FlyerForm(request.POST, request.FILES)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.user = request.user
            cart.save()
            return redirect('/cart')  
    else:
        form = FlyerForm()
    return render(request, 'shop/flyer.html', {'form': form})

@login_required
def poster(request):
    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.user = request.user
            cart.save()
            return redirect('/cart')  
    else:
        form = PosterForm()
    return render(request, 'shop/poster.html', {'form': form})

@login_required
def leaflet(request):
    if request.method == 'POST':
        form = LeafletForm(request.POST, request.FILES)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.user = request.user
            cart.save()
            return redirect('/cart')  
    else:
        form = LeafletForm()
    return render(request, 'shop/leaflet.html', {'form': form})

def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_cost = sum([item.get_total_cost() for item in cart_items])
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total_cost': total_cost})

def cart_item_delete(request, id):
    # if request.method == "POST":
    item = Cart.objects.get(id=id)
    item.delete()
    return redirect('/cart')

def create_order(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        return redirect('/cart')  # Перенаправление на страницу корзины, если она пуста

    for item in cart_items:
        Order.objects.create(
            product_name=item.product_name,
            user=item.user,
            format=item.format,
            colored=item.colored,
            sides=item.sides,
            paper_type=item.paper_type,
            extra_info=item.extra_info,
            file=item.file,
            amount=item.amount,
            cost=item.cost,
            work_status='new'
        )
    
    # Очистка корзины после создания заказа
    cart_items.delete()
    return redirect('/thankyou')



def add_notification(request):
    if request.method == 'POST':
        notification = Notification()
        notification.name = request.POST.get('name')
        notification.email = request.POST.get('email')
        notification.save()
    return HttpResponseRedirect("/")

def add_support(request):
    if request.method == 'POST':
        support = Support()
        support.name = request.POST.get('name')
        support.surname = request.POST.get('surname')
        support.email = request.POST.get('email')
        support.message = request.POST.get('message')
        support.save()
    return HttpResponseRedirect("/")