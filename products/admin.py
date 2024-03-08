from django.contrib import admin


from .models import Product, Comment


class ProductCommentIlines(admin.TabularInline):
    model = Comment
    fields = ['user', 'product', 'text','active','stars']
    extra = 1




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title', 'price', 'date_time_created', 'active', ]
    inlines = [
        ProductCommentIlines,
    ]
    

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display=['user', 'product', 'date_time_created', 'active','stars']