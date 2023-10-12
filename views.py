from django.shortcuts import render, get_object_or_404
from .models import Client
from .models import Product


def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'myapp/client_detail.html', {'client': client})
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'myapp/client_list2.html', {'clients': clients})
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'myapp/product_detail3.html', {'product': product})
def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list4.html', {'products': products})
