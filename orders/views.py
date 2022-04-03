from django.shortcuts import render
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="login")
def create_order(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            order = Order.objects.create(user=request.user)
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(request, "orders/order/created.html", {'order' : order})

    else:
        form = OrderCreateForm(instance=request.user.profile)
        return render(request, "orders/create.html", {"cart" : cart, "form" : form})