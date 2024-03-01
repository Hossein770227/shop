from django.shortcuts import render


from .cart import Cart


def cart_create_view(request):
    cart=Cart(request)
    return render(request, 'cart/cart_create.html',{'cart':cart})
