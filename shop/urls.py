from django.urls import path
from .views import index, store, checkout, product

urlpatterns = [
    path('index/' , index, name="index"),
    path('store/', store, name="store"),
    path('checkout/', checkout, name="checkout"),
    path('product/', product, name="product"),
]
