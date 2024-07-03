from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login
from .models import Product, ShoppingCart
from .forms import UserRegistrationForm, LoginForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.sessions.models import Session

# Create your views here.

@staff_member_required
def my_custom_viewer(request):
    context = {
        'title': 'my custom admin page'
    }
    return render(request, 'admin/my_custom_template.html', context)

def index(request):
    product_list = Product.objects.all()
    return  render(request, 'home.html', {'productos': product_list}) 

def product(request, product_id):
    try:
        get_product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, "product.html", {"product": get_product})

def profile(request):
    return HttpResponse(request.session.session_key)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cart_items = ShoppingCart.objects.filter(session_id=request.session.session_key)   
            
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            #Log the user in and redirect to homepage
            user = authenticate(username=new_user.username, password=form.cleaned_data['password'])
            
            for item in cart_items:
                item.user = new_user
                item.save()

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


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key
    
    cart_item, created = ShoppingCart.objects.get_or_create(session_id=session_id, product_id=str(product.id))
    cart_item.amount += 1
    cart_item.save()
    return redirect('view_cart')

def view_cart(request):
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    print(f"Session ID: {session_id}")  # Debugging statement

    if session_id is None:
        return HttpResponse("Session ID is None")

    try:
        if request.user.is_authenticated:
            print('find shopping cart with user id')
            cart_items = ShoppingCart.objects.filter(user=request.user)
        else:
            cart_items = ShoppingCart.objects.filter(session_id=session_id)
            print(f"Cart items: {cart_items}")  # Debugging statement
    except Exception as e:
        return HttpResponse(f"Error: {e}")

    if not cart_items.exists():
        return HttpResponse("No items in cart")

    products = []
    total_price = 0

    for item in cart_items:
        prod = Product.objects.get(id=item.product_id)
        products.append(prod)
        total_price = total_price + prod.price

    return render(request, 'shoppingcar.html', {'cart_items': cart_items, 'products': products, 'total_price': total_price})


# AI GENERATED, NOT CHECKED YET
""" def buy_cart(request):
# If user is not authenticated
    if not request.user.is_authenticated:
        return redirect('register')  # Redirect to registration page

    session_id = request.session.session_key
    cart_items = ShoppingCart.objects.filter(session_id=session_id)

    if not cart_items.exists():
        return HttpResponse("No items in cart")

    total_price = 0

    for item in cart_items:
        prod = Product.objects.get(id=item.product_id)
        total_price += prod.price
    # Purchase products
    for item in cart_items:
        prod = Product.objects.get(id=item.product_id)
        prod.quantity -= 1
        if prod.quantity == 0:
            prod.delete()
        else:
            prod.save()

        item.delete()  # Remove the cart item after purchase

    return render(request, 'purchase_successful.html', {'total_price': total_price}) """