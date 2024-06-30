from django.shortcuts import render

from catalog.models import Product, Contact, Category


def home(request):
    prod_list = Product.objects.all()
    context = {
        'object_list': prod_list
    }
    if request.method == 'GET':
        print(f'{prod_list}')
    return render(request, 'main/home.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("massage")
        print(f"{name}, ({email}): {massage}")
    contact_list = Contact.objects.all()
    context = {
        'object_list': contact_list
    }
    return render(request, 'main/contact.html', context)


def product(request, pk):
    product_obj = Product.objects.get(pk=pk)
    context = {'object': product_obj}
    return render(request, 'main/product.html', context)


def add_product(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }
    if request.method == 'POST':
        name = request.POST.get("name"),
        description = request.POST.get("description"),
        image = request.POST.get("image"),
        category = request.POST.get("category"),
        price = request.POST.get("price")
        print(f'{name} {description} {image} {category} {price}')
        # Product.objects.create(name=request.POST.get("name"),
        #                        description=request.POST.get("description"),
        #                        image=request.POST.get("image"),
        #                        category=request.POST.get("category"),
        #                        price=request.POST.get("price"))
    return render(request, 'main/add_product.html', context)
