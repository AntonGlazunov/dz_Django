from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("massage")
        print(f"{name}, ({email}): {massage}")
    return render(request, 'main/contact.html')
