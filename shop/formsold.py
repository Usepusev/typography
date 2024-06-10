from django import forms
from .models import Cart, Product

class CartForm(forms.ModelForm):
    FORMAT_CHOICES = [(item, item) for item in Product.objects.values_list('format', flat=True).distinct()]
    COLORED_CHOICES = [(item, item) for item in Product.objects.values_list('colored', flat=True).distinct()]
    SIDES_CHOICES = [(item, item) for item in Product.objects.values_list('sides', flat=True).distinct()]
    PAPER_TYPE_CHOICES = [(item, item) for item in Product.objects.values_list('paper_type', flat=True).distinct()]
    
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
        if commit:
            cart.save()
        return cart

    def calculate_cost(self, cart):
        product = Product.objects.get(format=cart.format, colored=cart.colored, sides=cart.sides, paper_type=cart.paper_type)
        return product.price_per_unit * cart.amount
