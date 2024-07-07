from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import contact, ProductListView, ProductDetailView, ProductCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contact', contact, name='contact'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product_form', ProductCreateView.as_view(), name='add_product'),
]
