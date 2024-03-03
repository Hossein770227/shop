from django.shortcuts import render, get_object_or_404
from django.views import generic


from .models import Product, Comment
from .fomrs import CommentForm

class ProductListView(generic.ListView):
    model = Product
    paginate_by= '2'
    template_name = 'products/product_list.html'
    context_object_name = 'products'


# class ProductDetailView(generic.DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
#     context_object_name = 'product'
    
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all().filter(active= True)
    if request.method == 'POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit= False)
            new_comment.user= request.user
            new_comment.product= product
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
        
    return render(request, 'products/product_detail.html',{'product':product, 'comments':comments, 'comment_form':comment_form} )