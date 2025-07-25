from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import Product, Category
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
    category = request.GET.get('category')

    if category is not None:
        products = Product.objects.filter(category__title=category)
        return render(request, "store.html", {'products' : products})

    products = Product.objects.all()
    return render(request, "store.html", {'products' : products})


def detail(request, id:int, title:str):
    product = get_object_or_404(Product, id=id)
    return render(request, "product.html", {'product' : product})


@require_POST
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))

    get_object_or_404(Product, id=product_id)
    
    return render(request, "cart.html")

def cart(request):
    pass
