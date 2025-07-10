from .models import Product , Cart
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=Product)
def soft_delete_cart(sender, instance,created, **kwargs):
    if not created:
        if instance.deleted:
            carts = Cart.objects.filter(product=instance)
            for cart in carts:
                cart.delete()