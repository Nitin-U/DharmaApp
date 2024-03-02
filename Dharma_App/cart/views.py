from django.shortcuts import render, redirect
from .models import User, Product
from django.views import View
from .forms import AddProductForm
from django.contrib import messages

# Create your views here.
# Function based method
# def productlist(request):
#     current_user = request.user  # Since we are using Django's built-in authentication system, we request the current user associated to product

#     products = Product.objects.filter(seller=current_user) # User associated to their particular product

#     return render (request, 'cart/productlist.html', {'products': products, 'user': current_user})

# Class based method
class ProductList(View):
    def get(self, request):
        current_user = request.user  # Since we are using Django's built-in authentication system, we request the current user associated to product

        products = Product.objects.filter(seller=current_user) # User associated to their particular product

        return render (request, 'cart/productlist.html', {'products': products, 'user': current_user})
    
class AddProduct(View):
    def get(self, request):
        productform = AddProductForm()
        return render (request, 'cart/addproduct.html', {
            'form': productform
        })
    
    def post(self, request):
        productform = AddProductForm(request.POST)
        # print(productform)
        if productform.is_valid():
            # productform.save()
            obj = productform.save(commit=False)
            obj.seller = request.user
            obj.save()
            messages.success(request, "Product Added Successfully")
            return redirect('cart:productlist')

        else:
            messages.error(request, "Sorry, An Error Occured")
            return render(request, 'cart/addproduct.html', {
                'form': productform
            })
        
class DeleteProduct(View):
    def post(self, request):
        data = request.POST
        # print(data)
        id = data.get('id')
        # print(id)
        productdata = Product.objects.get(id=id)
        # print(productdata)
        productdata.delete()
        messages.error(request, "Data Deleted Successfully")
        return redirect('cart:productlist')
    
class EditProduct(View):
    def get(self, request, id):
        # print(id)
        productdata = Product.objects.get(id=id)
        productform = AddProductForm(instance=productdata)
        return render(request, 'cart/editproduct.html', {
            'form': productform
        })
    
    def post(self, request, id):
        productdata = Product.objects.get(id=id)
        productform = AddProductForm(request.POST, instance=productdata)
        if productform.is_valid():
            productform.save()
            messages.error(request, "Data Edited Successfully")
            return redirect('cart:productlist')