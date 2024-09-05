from django import forms 
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product_Id',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier'
        }
        widgets = {
            'product_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g 1'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'S12345'}),
            'price': forms.NumberInput(attrs={'class': 'form-control','placeholder':'price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control','placeholder':'e.g 1'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ABC'}),
        }