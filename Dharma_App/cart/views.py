from django.shortcuts import render
from .models import User, Product

# Create your views here.
def productlist(request):
    current_user = request.user  # Since we are using Django's built-in authentication system, we request the current user associated to product

    products = Product.objects.filter(seller=current_user) # User associated to their particular product

    return render (request, 'cart/productlist.html', {'products': products, 'user': current_user})