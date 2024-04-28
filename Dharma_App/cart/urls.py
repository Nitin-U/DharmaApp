from django.urls import path
from . import views
from .views import ProductList, AddProduct, DeleteProduct, EditProduct

app_name = 'cart'  # Define the namespace for the cart app

urlpatterns = [
    path('productlist', ProductList.as_view(), name='productlist'),
    path('addproduct/', AddProduct.as_view(), name='addproduct'),
    path('editproduct/<int:id>', EditProduct.as_view(), name='editproduct'),
    path('deleteproduct/', DeleteProduct.as_view(), name='deleteproduct'),
    path('searchproduct', views.searchproduct, name='searchproduct'),
    path('dashboard_base', views.dashboard_base, name='dashboard_base'),
    path('seller_dashboard', views.seller_dashboard, name='seller_dashboard'),
    path('seller_addproduct', views.seller_addproduct, name='seller_addproduct'),
    path('seller_manageproduct', views.seller_manageproduct, name='seller_manageproduct'),
    path('product_detailpage', views.product_detailpage, name='product_detailpage'),
]
