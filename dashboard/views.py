from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product ,Order
from .forms import ProductForm
from django.contrib.auth.models import User
# Create your views here.

@login_required
def staff_details(request,pk):

    product_count=Product.objects.count()
    worker= User.objects.get(id=pk)
    context={
        'product_count':product_count,
        'worker':worker,
    }
    return render(request, 'dashboard/staff-details.html',context)

@login_required
def index(request):
    orders=Order.objects.all()
    product_count=Product.objects.count()
    context={
    'product_count':product_count,
    'orders':orders,
    }
    return render(request, 'dashboard/index.html',context)
@login_required
def staff(request):
    worker=User.objects.all()
    product_count=Product.objects.count()
    context={
    'product_count':product_count,
    'worker':worker,
    }
    return render(request, 'dashboard/staff.html',context)
@login_required
def product(request):
    items=Product.objects.all()
    #items=Product.objects.raw('SELECT * FROM dashboard_product')
    product_count=Product.objects.count()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid :
            form.save()
            return redirect('dashboard-product')
    else :
        form =ProductForm()
    context={
    'items':items,
    'form':form,
    'product_count':product_count,
    }
    return render(request, 'dashboard/product.html',context)
@login_required
def order(request):
    return render(request, 'dashboard/order.html')
@login_required
def product_delete(request,pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product-delete.html')
@login_required
def product_update(request,pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        form =ProductForm(request.POST,instance=item)
        if form.is_valid:
            form.save()
            return redirect('dashboard-product')
    else :
        form =ProductForm(instance=item)
    context={
        'form': form,
    }
    return render(request, 'dashboard/product-update.html',context)
@login_required
def order(request):
    orders=Order.objects.all()
    context={
    'orders':orders,
    }
    return render(request, 'dashboard/order.html',context)
