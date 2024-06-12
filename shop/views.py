from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, Notification, Support, Order, Bill
from .forms import BlankForm, BookletForm, FlyerForm, PosterForm, LeafletForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from django.conf import settings
import os
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

    # Создание заказов
    orders = []
    for item in cart_items:
        order = Order.objects.create(
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
        orders.append(order)
    
    # Создание чека
    bill = Bill.objects.create(user=request.user)
    bill.order.set(orders)
    bill.save()

    # Создание PDF чека
    order_details = {
        "order_id": bill.bill_id,
        "created_at": bill.created_at.strftime('%d.%m.%Y'),
        "items": [
            {
                "product_name": order.product_name,
                "format": order.format,
                "colored": order.color,
                "sides": order.sides,
                "paper_type": order.paper_type,
                "extra_info": order.extra_info,
                "amount": order.amount,
                "cost": order.cost,
            }
            for order in orders
        ]
    }

    pdf_path = os.path.join(settings.MEDIA_ROOT, 'bills', f'invoice_{bill.bill_id}.pdf')
    generate_invoice(order_details, pdf_path)
    bill.file.name = f'bills/invoice_{bill.bill_id}.pdf'  # Устанавливаем путь к файлу
    bill.save()
    
    # Очистка корзины после создания заказа
    cart_items.delete()
    return redirect('/thankyou')


@csrf_exempt
def add_notification(request):
    if request.method == 'POST':
        notification = Notification()
        notification.name = request.POST.get('name')
        notification.email = request.POST.get('email')
        notification.save()
    return HttpResponseRedirect('/')

def add_support(request):
    if request.method == 'POST':
        support = Support()
        support.name = request.POST.get('name')
        support.surname = request.POST.get('surname')
        support.email = request.POST.get('email')
        support.message = request.POST.get('message')
        support.save()
    return HttpResponseRedirect("/")

def generate_invoice(order, file_path):
    # Создание canvas
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4
    
    # Регистрация шрифта Times New Roman
    font_path = os.path.join(settings.BASE_DIR, 'shop', 'fonts', 'times.ttf')
    pdfmetrics.registerFont(TTFont('TimesNewRoman', font_path))
    c.setFont("TimesNewRoman", 12)
    
    # Заголовок в центре
    c.setFont("TimesNewRoman", 14)
    c.drawCentredString(105 * mm, 270 * mm, "СПБ ГБПОУ «АУГСГИП»")
    
    # Заголовок заказа
    c.setFont("TimesNewRoman", 12)
    c.drawCentredString(105 * mm, 260 * mm, "ЗАКАЗ на выполнение полиграфических услуг")
    c.drawCentredString(105 * mm, 250 * mm, f"№ {order['order_id']}")
    
    # Дата справа
    c.drawRightString(200 * mm, 250 * mm, f"дата {order['created_at']}")
    
    # Таблица данных
    data = [
        ["№", "Наименование", "формат", "цветность", "сторон", "бумага г/кв.м.", "дополнительно", "кол-во", "стоимость", "сумма"],
    ]
    
    total_sum = 0
    for idx, item in enumerate(order['items'], start=1):
        data.append([
            idx, item['product_name'], item['format'], item['colored'], item['sides'],
            item['paper_type'], item['extra_info'], item['amount'], item['cost'], item['amount'] * item['cost']
        ])
        total_sum += item['amount'] * item['cost']
    
    data.append(["", "", "", "", "", "", "", "", "ИТОГО", total_sum])
    
    table = Table(data, colWidths=[10 * mm, 30 * mm, 15 * mm, 15 * mm, 10 * mm, 25 * mm, 30 * mm, 15 * mm, 15 * mm, 20 * mm])
    table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'TimesNewRoman'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'TimesNewRoman'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    table.wrapOn(c, width, height)
    table.drawOn(c, 10 * mm, 150 * mm)
    
    # Подвал с реквизитами для оплаты
    c.drawString(10 * mm, 50 * mm, "Реквизиты для оплаты")
    c.drawString(10 * mm, 45 * mm, "ИНН: 1234567890")
    c.drawString(10 * mm, 40 * mm, "КПП: 044521234")
    c.drawString(10 * mm, 35 * mm, "РС: 40702810123450101230")
    c.drawString(10 * mm, 30 * mm, "ЛС: 250405")
    
    c.save()
    print(f"Invoice saved to {file_path}")
    