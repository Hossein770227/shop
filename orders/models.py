from django.db import models
from django.contrib.auth import get_user_model



class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    is_paid = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=700)
    order_notes = models.TextField(blank= True)

    date_time_created = models.DateTimeField(auto_now_add= True)
    date_time_modified = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'order {self.id}'


class OrderItem(models.Model):

    order = models.ForeignKey(Order,  on_delete= models.CASCADE, related_name= 'items')
    product = models.ForeignKey('products.Product', on_delete= models.CASCADE, related_name= 'orderitems')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'order{self.order.id} product:{self.product} quantity {self.quantity} with(price {self.price}) '