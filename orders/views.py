from django.shortcuts import render, redirect

from cart.cart import Cart
from .forms import OrderForm
from .models import Order, OrderItem


def order_create_view(request):
    order_form = OrderForm()
    cart=Cart(request)
    if len(cart) == 0:
        return redirect('product:product_list')
    
    if request.method =='POST':
        order_form= OrderForm(request.POST,)

        if order_form.is_valid():
            order_obj=order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.sava()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                order = order_obj, 
                product = product, 
                quantity = item['quantity'],
                price = product.price , 

                )

            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

            # request.session['order_obj']= order_obj.id

            # return redirect('product:product_list')
    return render(request, 'orders/order_create.html', {'form':order_form})