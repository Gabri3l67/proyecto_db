from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login
from .models import Productos
from .forms import UserRegistrationForm, LoginForm
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

def profile(request):
    return HttpResponse(request.session.session_key)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            
            #Log the user in and redirect to homepage
            user = authenticate(username=new_user.username, password=form.cleaned_data['password'])
            login(request, user)
            return redirect('index') 
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', { 'form' : form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                print('ola')
                
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})