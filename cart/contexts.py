from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    """
    The contents of a basket will be available during the session
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.product_price
        item_total = quantity * product.product_price
        product_count += quantity
        cart_items.append({ 'id':id, 'quantity': quantity, 'product': product, 'item_total': item_total })

    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count}