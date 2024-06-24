from django.shortcuts import render
from django.views import generic

from catalog.models import Product, Contact


def home(request):
    if request.method == 'GET':
        prod_list = Product.objects.all()[:5]
        print(f'{prod_list}')
    return render(request, 'main/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("massage")
        print(f"{name}, ({email}): {massage}")
    return render(request, 'main/contact.html')


class ProductListView(generic.ListView):
    model = Product
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()[:5]
        return context


class ContactListView(generic.ListView):
    model = Contact
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactListView, self).get_context_data(**kwargs)
        context['contact_list'] = Contact.objects.all()
        return context
