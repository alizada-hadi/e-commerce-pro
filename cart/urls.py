from django.urls import path
from . import views


app_name = "cart"

urlpatterns = [
    path("", views.cart_detail, name="cart_detail"),  
    path("add/<str:product_id>/", views.add_to_cart, name="cart_add"), 
    path("remove/<str:product_id>/", views.remove_from_cart, name="cart_remove")
]

