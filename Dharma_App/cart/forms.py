from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name', 'product_type', 'product_category', 'product_description', 'product_quantity', 'product_price', 'product_stock']