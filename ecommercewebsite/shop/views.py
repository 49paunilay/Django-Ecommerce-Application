from django.shortcuts import render,redirect
from .models import Product,Order,ContactUs
from django.core.paginator import Paginator
import time
# Create your views here.
def index(request):
    product_object = Product.objects.all()
    context={
        'product_object':product_object
    }
    itemName = request.GET.get('item_name')
    if itemName !='' and itemName!=None:
        product_object = product_object.filter(title__icontains=itemName)
        paginator = Paginator(product_object,2)
        page = request.GET.get('page')
        product_object = paginator.get_page(page)
        context={
            'product_object':product_object
        }
    return render(request,'shop/index.html',context)

def details(request,id):
    particular_item = Product.objects.get(id=id)
    context={
        'particular_item':particular_item
    }
    return render(request,'shop/detail.html',context)

def cart_details(request):
    if(request.method=="POST"):
        items = request.POST.get('items')
        fname = request.POST.get('first_name',"")
        lname = request.POST.get('last_name',"")
        email = request.POST.get('Email',"")
        username = request.POST.get('username',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zip',"")
        totalPrice = request.POST.get('total',1.0)
        order = Order()
        order.items = items
        order.fname = fname
        order.lname = lname
        order.email = email
        order.username = username
        order.city =city
        order.state = state
        order.zipcode =zipcode
        order.totalPrice = totalPrice
        order.save()
        time.sleep(5)
        return redirect('/')
    return render(request,'shop/cartDetails.html')

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email_address')
        phone = request.POST.get('number')
        issue = request.POST.get('issue')
        contactus = ContactUs()
        contactus.email = email
        contactus.phone = phone
        contactus.issue = issue
        contactus.save()
        return redirect('/')
    return render(request,'shop/contact.html')