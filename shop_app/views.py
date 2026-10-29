from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}

    return render(request, 'home.html', context)

def products(request):
    product_list = [
        {"name": "Laptop", "price": 2500},
        {"name": "Mouse", "price": 80},
        {"name": "Keyboard", "price": 150},
        {"name": "Monitor", "price": 700},
    ]
    context = {"products": product_list}

    return render(request, 'products.html', context)