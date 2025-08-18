from .cart import Cart
from .models import Product
from decimal import Decimal



def cart_add(request):
    cart = Cart(request)

    if cart.cart:
        product_ids = cart.product_ids()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            cart[str(product.id)]['product'] = product


        sub_total = 0
        cart_quantity = 0
        for item in cart:
            item['total'] = Decimal(item['price']) * item['quantity']
            sub_total += item['total']
            cart_quantity += item['quantity']

        cart.cart_quantity = cart_quantity
        cart.sub_total = sub_total
        return {'cart': cart}
    else:
        return {'cart': None}