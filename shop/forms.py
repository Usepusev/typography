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
    format = forms.ChoiceField(choices=FORMAT_CHOICES)
    colored = forms.ChoiceField(choices=COLORED_CHOICES)
    sides = forms.ChoiceField(choices=SIDES_CHOICES)
    paper_type = forms.ChoiceField(choices=PAPER_TYPE_CHOICES)
    amount = forms.IntegerField(initial=1, validators=[MinValueValidator(1)])
    extra_info = forms.CharField(required=False)
    file = forms.FileField(required=True)

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
    format = forms.ChoiceField(choices=FORMAT_CHOICES)
    colored = forms.ChoiceField(choices=COLORED_CHOICES)
    sides = forms.ChoiceField(choices=SIDES_CHOICES)
    paper_type = forms.ChoiceField(choices=PAPER_TYPE_CHOICES)
    amount = forms.IntegerField(initial=1)
    extra_info = forms.CharField(required=False)
    file = forms.FileField(required=True)

    class Meta:
        model = Cart
        fields = ['format', 'colored', 'sides', 'paper_type', 'amount', 'file', 'extra_info']

    def save(self, commit=True):
        cart = super().save(commit=False)
        cart.cost = self.calculate_cost(cart)
        cart.product_name = 'Буклет'
        if commit:
            cart.save()
        return cart

    def calculate_cost(self, cart):
        product = Product.objects.get(product_name=cart.product_name ,format=cart.format, colored=cart.colored, sides=cart.sides, paper_type=cart.paper_type)
        return product.price_per_unit * cart.amount
