from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    FORMAT_CHOICES = [
        ('A3', 'A3'),
        ('A4', 'A4'),
        ('A5', 'A5'),
    ]
    format = models.CharField(max_length=3, choices=FORMAT_CHOICES)
    COLORED_CHOICES = [
        ('black_white', 'Ч/Б'),
        ('color', 'Цветное'),
    ]
    colored = models.CharField(max_length=20, choices=COLORED_CHOICES)
    SIDES_CHOICES = [
        (1, '1 сторона'),
        (2, '2 стороны'),
    ]
    sides = models.IntegerField(choices=SIDES_CHOICES)
    PAPER_TYPE_CHOICES = [
        (80, '80 г/м²'),
        (90, '90 г/м²'),
        (120, '120 г/м²'),
    ]
    paper_type = models.IntegerField(choices=PAPER_TYPE_CHOICES)
    extra_info = models.TextField(blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='product_images', null=True, blank=True)
    slug = models.SlugField('URL', max_length=255,null=True, unique=True, allow_unicode=True)

    @property
    def color(self):
        if self.colored == 'black_white':
            return 'Ч/Б'
        elif self.colored == 'color':
            return 'Цветное'
    
    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    format = models.CharField(max_length=100)
    colored = models.CharField(max_length=100)
    sides = models.CharField(max_length=100)
    paper_type = models.CharField(max_length=100)
    extra_info = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/')
    amount = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f'Cart {self.id} for {self.user.username}'

    def get_total_cost(self):
        return self.amount * self.cost
    @property
    def color(self):
        if self.colored == 'black_white':
            return 'Ч/Б'
        elif self.colored == 'color':
            return 'Цветное'
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    format = models.CharField(max_length=100)
    colored = models.CharField(max_length=100)
    sides = models.CharField(max_length=100)
    paper_type = models.CharField(max_length=100)
    extra_info = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/')
    amount = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('in_progress', 'В процессе'),
        ('completed', 'Выполнен'),
        ('cancelled', 'Отменён'),
    )
    work_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def status(self):
        if self.work_status == 'new':
            return 'Новый, ожидает оплаты'
        elif self.work_status == 'in_progress':
            return 'В процессе'
        elif self.work_status == 'completed':
            return 'Выполнен'
        elif self.work_status == 'cancelled':
            return 'Отменён'
    @property
    def color(self):
        if self.colored == 'black_white':
            return 'Ч/Б'
        elif self.colored == 'color':
            return 'Цветное'
    def __str__(self): 
        return f'Order {self.order_id} for {self.user.username}'

    def get_total_cost(self):
        return self.amount * self.cost
    
class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='bills/')
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.ManyToManyField('Order', related_name='bills')
    status = models.CharField(max_length=20, default='new')
    @property
    def billstatus(self):
        if self.status == 'new':
            return 'Новый, ожидает оплаты'
        elif self.status == 'in_progress':
            return 'В процессе'
        elif self.status == 'completed':
            return 'Выполнен'
        elif self.status == 'cancelled':
            return 'Отменён'
class Notification(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Support(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()