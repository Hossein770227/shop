from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _








class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    is_paid = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100, verbose_name= _('first name'))
    last_name =models.CharField(max_length=100,verbose_name= _('last name'))
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=700,verbose_name= _('adress'))
    order_notes = models.TextField(blank= True)

    zarinpal_authority = models.CharField(max_length=255, blank=True)

    date_time_created = models.DateTimeField(auto_now_add= True)
    date_time_modified = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'order {self.id}'

    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())

class OrderItem(models.Model):

    order = models.ForeignKey(Order,  on_delete= models.CASCADE, related_name= 'items')
    product = models.ForeignKey('products.Product', on_delete= models.CASCADE, related_name= 'orderitems')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'order{self.order.id} product:{self.product} quantity {self.quantity} with(price {self.price}) '