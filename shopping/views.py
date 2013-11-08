from django.shortcuts import render
from django.http import HttpResponse
from shopping.models import *
from datetime import datetime

# Create your views here.
def index(request):
    items = ShoppingItem.objects.all()
    context = {'shoplist' : items}
    return render(request, 'shopping/index.html', context)

def create_shopping_item(request):
    if(request.method == 'POST'):
        form = ShoppingItemForm(request.POST)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.pub_date = datetime.now()
            shop.save()
            return redirect('/shopping/')
        
    else:
        shop = ShoppingItem()
        shoppingForm = ShoppingItemForm(instance = shop)
        return render(request, 'shopping/create_shopping_item.html', {'shoppingForm' : shoppingForm, 'request' : request})
    
    
    
