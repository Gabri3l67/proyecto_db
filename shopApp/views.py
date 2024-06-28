from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Productos
# Create your views here.

def index(request):
    productos = Productos.objects.all()
    return  render(request, 'home.html', {'productos': productos}) 

def product(request, product_id):
    try:
        get_product = Productos.objects.get(pk=product_id)
    except Productos.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, "product.html", {"product": get_product})