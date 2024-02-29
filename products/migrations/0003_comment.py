# Generated by Django 5.0.2 on 2024-02-29 06:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price_with_discount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='your comment')),
                ('date_time_created', models.DateTimeField(auto_now_add=True, verbose_name=' date time created')),
                ('date_time_modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('stars', models.CharField(choices=[('1', 'verybad'), ('2', 'bad'), ('3', 'normal'), ('4', 'good'), ('5', 'prefect')], max_length=15, verbose_name='date time modified')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]