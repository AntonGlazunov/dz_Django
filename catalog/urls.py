from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import contact, product, add_product, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('home/contact', contact, name='contact'),
    path('home/<int:pk>', product, name='product_detail'),
    path('home/add_prod', add_product, name='add_product'),
]
