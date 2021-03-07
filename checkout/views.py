from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ISPN5AbTLswkfEnRMl1vGz6pty9s4oBG0BmmrbfguKdw61pk8STD9g9VZEZHyZrGDGW8wSYu9kcxw1WeLIc4Zze00EPXtrtpH',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
