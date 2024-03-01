from django.shortcuts import render, get_object_or_404, redirect 



from .cart import Cart
from products.models import Product
from .forms import AddToProductForm


def cart_create_view(request):
    cart=Cart(request)

    for item in cart:
        item['product_update_quantity_form']=AddToProductForm(
            initial={'quantity':item['quantity'], "inplace":True}
        )
        
    return render(request, 'cart/cart_create.html',{'cart':cart})


def add_to_cart_view(request, product_id):
    cart= Cart(request)
    product= get_object_or_404(Product, id=product_id)

    form= AddToProductForm(request.POST)

    if form.is_valid():

        cleaned_data= form.cleaned_data
        quantity= cleaned_data['quantity']

        cart.add(product, quantity, replace_current_quantity=cleaned_data['inplace'])

    return redirect('cart:cart_create')


def remove_from_cart(request, product_id):

    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_create')