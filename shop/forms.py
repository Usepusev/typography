from django import forms
from .models import Cart, Product
from django.core.validators import MinValueValidator
class BlankForm(forms.ModelForm):
    FORMAT_CHOICES = [
        ('A3', 'A3'),
        ('A4', 'A4'),
    ]
    SIDES_CHOICES = [
        (1, '1 сторона'),
        (2, '2 стороны'),
    ]
    COLORED_CHOICES = [
        ('black_white', 'Ч/Б'),
    ]
    PAPER_TYPE_CHOICES = [
        (80, '80 г/м²'),
    ]
    format = forms.ChoiceField(label='Формат', choices=FORMAT_CHOICES)
    colored = forms.ChoiceField(label='Цвет', choices=COLORED_CHOICES)
    sides = forms.ChoiceField(label='Стороны', choices=SIDES_CHOICES)
    paper_type = forms.ChoiceField(label='Бумага', choices=PAPER_TYPE_CHOICES)
    amount = forms.IntegerField(label='Количество', initial=1, validators=[MinValueValidator(1)])
    extra_info = forms.CharField(label='Доп. информация', required=False)
    file = forms.FileField(label='Файл', required=True)

    class Meta:
        model = Cart
        fields = ['format', 'colored', 'sides', 'paper_type', 'amount', 'file', 'extra_info']

    def save(self, commit=True):
        cart = super().save(commit=False)
        cart.cost = self.calculate_cost(cart)
        cart.product_name = 'Бланк'
        if commit:
            cart.save()
        return cart

    def calculate_cost(self, cart):
        product = Product.objects.get(format=cart.format, colored=cart.colored, sides=cart.sides, paper_type=cart.paper_type)
        return product.price_per_unit * cart.amount

class BookletForm(forms.ModelForm):
    FORMAT_CHOICES = [
        ('A4', 'A4'),
    ]
    SIDES_CHOICES = [
        (2, '2 стороны'),
    ]
    COLORED_CHOICES = [
        ('color', 'Цветное'),
    ]
    PAPER_TYPE_CHOICES = [
        (120, '120 г/м²'),
    ]
    format = forms.ChoiceField(label='Формат', choices=FORMAT_CHOICES)
    colored = forms.ChoiceField(label='Цвет', choices=COLORED_CHOICES)
    sides = forms.ChoiceField(label='Стороны', choices=SIDES_CHOICES)
    paper_type = forms.ChoiceField(label='Бумага', choices=PAPER_TYPE_CHOICES)
    amount = forms.IntegerField(label='Количество', initial=1,  validators=[MinValueValidator(1)])
    extra_info = forms.CharField(label='Доп. информация', required=False)
    file = forms.FileField(label='Файл', required=True)

    class Meta:
        model = Cart
        fields = ['format', 'colored', 'sides', 'paper_type', 'amount', 'file', 'extra_info']

    def save(self, commit=True):
        cart = super().save(commit=False)
        cart.product_name = 'Евробуклет'
        cart.cost = self.calculate_cost(cart)
        if commit:
            cart.save()
        return cart

    def calculate_cost(self, cart):
        print(cart.product_name, cart.format, cart.colored, cart.sides, cart.paper_type)
        product = Product.objects.get(product_name=cart.product_name, format=cart.format, colored=cart.colored, sides=cart.sides, paper_type=cart.paper_type)
        return product.price_per_unit * cart.amount

class FlyerForm(forms.ModelForm):
    FORMAT_CHOICES = [
        ('A5', 'A5'),
    ]
    SIDES_CHOICES = [
        (1, '1 сторона'),
        (2, '2 стороны'),
    ]
    COLORED_CHOICES = [
        ('color', 'Цветное'),
    ]
    PAPER_TYPE_CHOICES = [
        (90, '90 г/м²'),
    ]
    format = forms.ChoiceField(label='Формат', choices=FORMAT_CHOICES)
    colored = forms.ChoiceField(label='Цвет', choices=COLORED_CHOICES)
    sides = forms.ChoiceField(label='Стороны', choices=SIDES_CHOICES)
    paper_type = forms.ChoiceField(label='Бумага', choices=PAPER_TYPE_CHOICES)
    amount = forms.IntegerField(label='Количество', initial=1, validators=[MinValueValidator(1)])
    extra_info = forms.CharField(label='Доп. информация', required=False)
    file = forms.FileField(label='Файл', required=True)

    class Meta:
        model = Cart
        fields = ['format', 'colored', 'sides', 'paper_type', 'amount', 'file', 'extra_info']

    def save(self, commit=True):
        cart = super().save(commit=False)
        cart.product_name = 'Флаер'
        cart.cost = self.calculate_cost(cart)
        if commit:
            cart.save()
        return cart

    def calculate_cost(self, cart):
        print(cart.product_name, cart.format, cart.colored, cart.sides, cart.paper_type)
        product = Product.objects.get(product_name=cart.product_name, format=cart.format, colored=cart.colored, sides=cart.sides, paper_type=cart.paper_type)
        return product.price_per_unit * cart.amount
class LeafletForm(forms.ModelForm):
    FORMAT_CHOICES = [
        ('A4', 'A4'),
    ]
    SIDES_CHOICES = [
        (1, '1 сторона'),
        (2, '2 стороны'),
    ]
    COLORED_CHOICES = [
        ('color', 'Цветное'),
    ]
    PAPER_TYPE_CHOICES = [
        (90, '90 г/м²'),
        (120, '120 г/м²'),
    ]
    format = forms.ChoiceField(label='Формат', choices=FORMAT_CHOICES)
    colored = forms.ChoiceField(label='Цвет', choices=COLORED_CHOICES)
    sides = forms.ChoiceField(label='Стороны',choices=SIDES_CHOICES)
    paper_type = forms.ChoiceField(label='Бумага', choices=PAPER_TYPE_CHOICES)
    amount = forms.IntegerField(label='Количество', initial=1, validators=[MinValueValidator(1)])
    extra_info = forms.CharField(label='Доп. информация',required=False)
    file = forms.FileField(label='Файл', required=True)

    class Meta:
        model = Cart
        fields = ['format', 'colored', 'sides', 'paper_type', 'amount', 'file', 'extra_info']

    def save(self, commit=True):
        cart = super().save(commit=False)
        cart.cost = self.calculate_cost(cart)
        cart.product_name = 'Флаер'
        if commit:
            cart.save()
        return cart

    def calculate_cost(self, cart):
        product = Product.objects.get(format=cart.format, colored=cart.colored, sides=cart.sides, paper_type=cart.paper_type)
        return product.price_per_unit * cart.amount
    
class PosterForm(forms.ModelForm):
    FORMAT_CHOICES = [
        ('A3', 'A3'),
    ]
    SIDES_CHOICES = [
        (1, '1 сторона'),
        (2, '2 стороны'),
    ]
    COLORED_CHOICES = [
        ('color', 'Цветное'),
    ]
    PAPER_TYPE_CHOICES = [
        (120, '120 г/м²'),
    ]
    format = forms.ChoiceField(label='Формат', choices=FORMAT_CHOICES)
    colored = forms.ChoiceField(label='Цвет', choices=COLORED_CHOICES)
    sides = forms.ChoiceField(label='Стороны',choices=SIDES_CHOICES)
    paper_type = forms.ChoiceField(label='Бумага', choices=PAPER_TYPE_CHOICES)
    amount = forms.IntegerField(label='Количество', initial=1, validators=[MinValueValidator(1)])
    extra_info = forms.CharField(label='Доп. информация', required=False)
    file = forms.FileField(label='Файл', required=True)

    class Meta:
        model = Cart
        fields = ['format', 'colored', 'sides', 'paper_type', 'amount', 'file', 'extra_info']

    def save(self, commit=True):
        cart = super().save(commit=False)
        cart.cost = self.calculate_cost(cart)
        cart.product_name = 'Плакат'
        if commit:
            cart.save()
        return cart

    def calculate_cost(self, cart):
        product = Product.objects.get(format=cart.format, colored=cart.colored, sides=cart.sides, paper_type=cart.paper_type)
        return product.price_per_unit * cart.amount