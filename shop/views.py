from django.shortcuts import render

# from django.http import HttpResponse


# Create your views here.
# def about(request, userName):
#     return HttpResponse("<h1>salaaam</h1>" + str(userName))


# def year(request, year):
#     return HttpResponse("<h1>sxsx</h1>" + str(year))


def index(request):
    return render(request, "index.html")


def checkout(request):
    return render(request, "checkout.html")


def store(request):
    return render(request, "store.html")


def product(request):
    return render(request, "product.html")
