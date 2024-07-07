from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product, Contact, UserFeedback


class ProductListView(ListView):
    model = Product
    fields = ()
    success_url = reverse_lazy('product_list')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("massage")
        UserFeedback.objects.create(name=name, email=email, massage=massage)
    contact_list = Contact.objects.all()
    context = {
        'object_list': contact_list
    }
    return render(request, 'catalog/contact.html', context)


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('product_list')
