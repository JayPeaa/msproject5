from django.shortcuts import render, redirect, reverse
from pages.forms import SubscriberForm
# Create your views here.


def view_cart(request):
    """See contents of cart also renders the subcribe
    form in the context"""
    context = {
        'newsletter_form': SubscriberForm()
    }
    return render(request, "cart.html", context)


def add_to_cart(request, id):
    """Add a qty of product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity

    request.session['cart'] = cart
    return redirect(reverse('products'))


def adjust_cart(request, id):
    """Adjust qty of items in cart"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_cart_item(request, id):
    """Delete of remove an item from the cart"""
    cart = request.session.get('cart', {})

    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
