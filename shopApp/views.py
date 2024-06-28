from django.shortcuts import render
from django.http import HttpResponse
from .models import Productos
# Create your views here.

def index(request):
    productos = Productos.objects.all()
    return  render(request, 'home.html', {'productos': productos}) 