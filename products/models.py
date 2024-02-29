from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


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
    

class Comment(models.Model):
    STARS_CHOICES = (
        ('1', _('verybad')),
        ('2', _('bad')),
        ('3', _('normal')),
        ('4', _('good')),
        ('5', _('prefect')),
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name=_('your comment'))
    date_time_created = models.DateTimeField(auto_now_add = True, verbose_name=_(' date time created'))
    date_time_modified = models.DateTimeField(auto_now= True)
    active = models.BooleanField(default= True)
    stars = models.CharField(choices=STARS_CHOICES, max_length=15,verbose_name=_('your score'))