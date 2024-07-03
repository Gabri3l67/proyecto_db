from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/my-custom-page/', views.my_custom_viewer, name='my_custom_viewer'),
    path("product/<int:product_id>", views.product, name="product"),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('buy_cart', views.buy_cart, name='buy_cart'),
    path('logout', views.logout_view, name='logout')
]