from ast import Return
from multiprocessing import context
from telnetlib import STATUS
from django.shortcuts import render
from django.http import HttpResponse
from .models import*
# Create your views here.
def home(request):

    orders = Orders.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    pending = orders.filter(status ='Pending').count()
    delivered = orders.filter(status ='Delivered').count() 

    context = {'orders':orders, 'customers':customers, 'total_customers': total_customers, 
    'total_orders': total_orders, 'pending': pending, 'delivered':delivered}

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products':products})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.orders_set.all()

    orders_count = orders.count()
    

    
    context = {'customer':customer, 'orders':orders, 'orders_count':orders_count}
    
    return render(request, 'accounts/customer.html', context)

def createOrder(request):

    context = {}

    return render(request, 'accounts/order_form.html', context)
