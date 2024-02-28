# Generated by Django 5.0.2 on 2024-02-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('short_description', models.CharField(blank=True, max_length=700)),
                ('price', models.PositiveIntegerField(default=0)),
                ('date_time_created', models.DateTimeField(auto_now_add=True)),
                ('date_time_modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]