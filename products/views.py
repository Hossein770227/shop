from django.shortcuts import render, get_object_or_404
from django.views import generic


from .models import Product

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


# class ProductDetailView(generic.DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
#     context_object_name = 'product'
    
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html',{'product':product} )