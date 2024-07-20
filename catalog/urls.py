from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import contact, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contact', contact, name='contact'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('create_product', ProductCreateView.as_view(), name='create_product'),
    path('edit_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
]
