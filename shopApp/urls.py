from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:product_id>", views.product, name="product"),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_user, name='login')
]