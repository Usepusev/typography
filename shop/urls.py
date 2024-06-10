from django.urls import path
from .views import index, prices, blank, cart, shop, thankyou, cart_item_delete, booklet, contact, leaflet, poster, flyer
from . import views
app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('prices/', prices, name='prices'),
    path('shop/', shop, name='shop'),
    path('blank/', blank, name='blank'),
    path('booklet/', booklet, name='booklet'),
    path('leaflet/', leaflet, name='leaflet'),
    path('poster/', poster, name='poster'),
    path('flyer/', flyer, name='flyer'),
    path('cart/', cart, name='cart'),
    path("delete/<int:id>/", cart_item_delete),
    path('contact/', contact, name='contact'),
    path('thankyou/', thankyou, name='thankyou'),
]