from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import home, contact, product, add_product

urlpatterns = [
    path('home', home, name='home'),
    path('home/contact', contact, name='contact'),
    path('home/<int:pk>', product, name='product_detail'),
    path('home/add_prod', add_product, name='add_product'),
]
