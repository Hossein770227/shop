from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length= 150)
    description = models.TextField()
    short_description = models.CharField(max_length= 700, blank= True)
    price = models.PositiveIntegerField(default= 0)
    price_with_discount = models.PositiveIntegerField(null=True, blank=True)
    date_time_created = models.DateTimeField(auto_now_add= True)
    date_time_modified = models.DateTimeField(auto_now= True)
    active = models.BooleanField(default= True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product:product_detail", args=[self.id])
    
