from django.urls import path

from catalog.views import home, contact, product

urlpatterns = [
    path('home', home, name='home'),
    path('home/contact', contact, name='contact'),
    path('home/<int:pk>', product, name='product_detail'),
]