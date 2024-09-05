
from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product
# Create your views here.

def home(request):
    return render(request, 'home.html')


# create a view
def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
            return redirect('product_list')
    return render(request, 'product.html', {'form': form})    
            
            
# read a view file
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


# uodate a view file
def update_view(request,product_id):
    product = Product.objects.get(product_id=product_id)
    form  = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'product.html', {'form': form})                             


def product_delete(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})
