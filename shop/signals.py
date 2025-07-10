from .models import Product , Cart, Order_products,Order
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=Product)
def soft_delete_cart(sender, instance,created, **kwargs):
    if not created:
        if instance.deleted:
            carts = Cart.objects.filter(product=instance)
            for cart in carts:
                cart.delete()


@receiver(post_save, sender=Product)
def soft_delete_order_product(sender, instance,created, **kwargs):
    if not created:
        if instance.deleted:
            order_products =  Order_products.objects.filter(product=instance)
            for order_product in order_products:
                order_product.delete()

@receiver(post_save, sender=Order)
def soft_delete_order_product(sender, instance,created, **kwargs):
    if not created:
        if instance.deleted:
            order_products =  Order_products.objects.filter(order=instance)
            for order_product in order_products:
                order_product.delete()