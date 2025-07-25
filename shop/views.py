from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

# from django.http import HttpResponse


# Create your views here.
# def about(request, userName):
#     return HttpResponse("<h1>salaaam</h1>" + str(userName))


# def year(request, year):
#     return HttpResponse("<h1>sxsx</h1>" + str(year))


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products' : products})


def checkout(request):
    return render(request, "checkout.html")


def store(request):
    return render(request, "store.html")


def detail(request, id:int, title:str):
    product = get_object_or_404(Product, id=id)
    return render(request, "product.html", {'product' : product})
