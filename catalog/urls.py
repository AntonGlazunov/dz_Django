from django.urls import path

from catalog.views import home, contact, ProductListView, ContactListView

urlpatterns = [
    path('home', ProductListView.as_view(), name='home'),
    path('home/contact', ContactListView.as_view(), name='contact'),
]