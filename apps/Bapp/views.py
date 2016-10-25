

# Create your views here.
from django.shortcuts import render, redirect
from ..login.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Product

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect(reverse('login:index'))
    user = User.objects.get(id = request.session['user_id'])
    # items = user.product_set.all().exclude(maker__id = request.session['user_id'])
    items = Product.objects.filter(users__id = request.session['user_id']).exclude(maker__id = request.session['user_id'])
    myItems = Product.objects.filter(maker__id=request.session['user_id'])
    OtherItems = Product.objects.exclude(maker__id=request.session['user_id'])
    context = {
    'items': items,
    'myItems': myItems,
    'OtherItems':OtherItems
    }

    return render (request, 'Bapp/index.html', context)

def item(request, id):
    try:
        item = Product.objects.get(id = id)
    except:
        return redirect(reverse('Bapp:dashboard'))
    context ={
    'users':item.users.all(),
    'name':item.name
    }

    return render (request, 'Bapp/item.html', context)
def removeitem(request, id):
    try:
        item = Product.objects.get(id=id)
    except:
        return redirect(reverse('Bapp:dashboard'))
    user = User.objects.get(id=request.session['user_id'])
    item.users.remove(user)
    return redirect(reverse('Bapp:dashboard'))
def delete(request, id):
    try:
        item = Product.objects.get(id=id)
    except:
        return redirect(reverse('Bapp:dashboard'))
    item.delete()
    return redirect(reverse('Bapp:dashboard'))

def additem(request, id):
    try:
        item = Product.objects.get(id=id)
    except:
        return redirect(reverse('Bapp:dashboard'))
    user=User.objects.get(id=request.session['user_id'])
    item.users.add(user)
    return redirect(reverse('Bapp:dashboard'))

def create(request):
    return render (request,'Bapp/create.html')
def add(request):
    if request.method != 'POST':
        return redirect(reverse('Bapp:dashboard'))
    name = request.POST['item']
    if len(name)<3:
        messages.error('item name should have at least 3 characters')
        return redirect(reverse('Bapp:create'))
    user = User.objects.get(id = request.session['user_id'])
    try:
        item = Product.objects.get(name = name)
    except:
        item = Product.objects.create(name = name, maker = user)
    item.users.add(user)
    return redirect(reverse('Bapp:dashboard'))
