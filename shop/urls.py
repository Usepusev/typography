from django.urls import path
from .views import index, prices, blank, cart, shop, thankyou, cart_item_delete, booklet, contact, leaflet, poster, flyer, add_notification, add_support
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
    path("cart/delete/<int:id>/", cart_item_delete),
    path('contact/', contact, name='contact'),
    path('thankyou/', thankyou, name='thankyou'),
    path('add_notification/', add_notification, name='add_notification'),
    path('contact/add_support/', add_support, name='add_support'),
    path('cart/create_order/', views.create_order, name='create_order'),
]