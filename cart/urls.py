from django.urls import path

from .views import cart_create_view

urlpatterns = [
    path('create/', cart_create_view, name='cart_create'),
]
