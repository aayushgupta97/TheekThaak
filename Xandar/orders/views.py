from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from core.models import OrderedItems, DeliveryAddresses, Customer, Wishlist, Cart, CartItems
from django.views.generic import ListView

# Create your views here.


def show_ordered_items(request):
    context = {}

    if request.method == 'POST':
        pass
    else:
        if request.user.is_authenticated:
            try:
                current_cart = Cart.objects.get(user_id=request.user.id)
                orders = CartItems.objects.filter(cart_id=current_cart)
                delivery_addresses = DeliveryAddresses.objects.filter(customer=request.user)
                context = {
                    'orders':orders,
                    'addresses': delivery_addresses
                }
            except Cart.DoesNotExist:
                context = {
                    'orders': False
                }
            return render(request, 'orders/checkout.html', context)
        else:
            return redirect('accounts:login_app')



def apply_coupon(request):
    coupon = request.GET['coupon']
    total = int(request.GET['total'])
    if coupon == 'FIRST':
        discount = 0.10 * total
    else:
        discount  = 0
    total = total-discount
    return HttpResponse(total)


def place_order(request):
    UserAddress = DeliveryAddresses()
    context={}
    for key, values in request.GET.items():
            setattr(UserAddress, key, request.GET[key])
            context[key]=values
    UserAddress.customer = request.user
    UserAddress.save()
    #UPDATE MAKE CART
    current_cart = Cart.objects.get(user_id=request.user.id)
    orders = CartItems.objects.filter(cart_id=current_cart)
    current_cart.delete()
    context['orders']=orders
    return render(request, 'orders/order_confirmed.html', context)

class get_delivery_addresses(ListView):
    template_name = 'orders/delivery_address.html'

    def get_queryset(self):
        queryset = DeliveryAddresses.objects.filter(customer=self.request.user)
        return queryset

