from django.urls import path

from .views import cart_create_view, add_to_cart_view


app_name= 'cart'

urlpatterns = [
    path('create/', cart_create_view, name='cart_create'),
    path('add/<int:product_id>/', add_to_cart_view, name='cart_add'),
]
