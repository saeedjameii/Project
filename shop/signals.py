from .models import Product , Cart, Order_products,Order
from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import User


@receiver(post_save, sender=Product)
def soft_delete_cart(sender, instance,created, **kwargs):
    if not created:
        if instance.deleted:
            carts = Cart.objects.filter(product=instance)
            for cart in carts:
                cart.delete()


@receiver(post_save, sender=User)
def soft_delete_cart(sender, instance,created, **kwargs):
    if not created:
        if instance.deleted:
            carts = Cart.objects.filter(user=instance)
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

@receiver(post_save, sender=User)
def soft_delete_order(sender, instance,created, **kwargs):
    if not created:
        if instance.deleted:
            orders =  Order.objects.filter(user=instance)
            for order in orders:
                order.delete()