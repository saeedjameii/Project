from django.db import models
from django.contrib.auth.models import User

class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

class BaseModel(models.Model):
    deleted = models.BooleanField(default=False, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()

    class Meta:
        abstract = True
    
    def delete(self, using =None, keep_parents =False):
        self.deleted = True
        self.save()


class category(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class product(BaseModel):
    title = models.CharField(max_length=100)
    contetnt = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField()
    quantity = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





class cart(BaseModel):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class order(BaseModel):
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(null=True)


class order_products(BaseModel):
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    # status = models.BooleanField(null=True)
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)


class payment(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    error_code = models.CharField(max_length=200)
