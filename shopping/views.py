from django.http import HttpResponse
from shopping.models import *
from shopping.forms import *
from datetime import datetime
from django.shortcuts import *
from django.db.models import get_model


modelforms = forms.ModelForm.__subclasses__()

def noSuchObject(request, msg):
    messages.error(request,msg)
    return redirect('/shopping/')
    
def get_modelform(model):
    try:
        return filter(lambda x:x.Meta.model == model, modelforms)[0] 
    except IndexError:
        print "No ModelForm for your model"

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
        print("Heia")
        shop = ShoppingItem()
        shoppingForm = ShoppingItemForm(instance = shop)
        return render(request, 'shopping/create_shopping_item.html', {'shoppingForm' : shoppingForm, 'request' : request})
    
def delete_shopping_item(request, case_id):
    if(request.method == 'POST'):
        item = ShoppingItem.objects.get(pk=case_id)
        item.delete()
        return HttpResponse("OK")

def edit_model(request, case_id):
    model = get_model('shopping', "ShoppingItem")
    modelform = get_modelform(model)
    try:
        item = model.objects.get(pk=case_id)
    except model.DoesNotExist:
        msg="Objekten finns inte"
        return noSuchObject(request,msg)
    if request.POST:
        form = modelform(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/shopping/')
    else:
        itemform = modelform(instance=item)
        context = {'itemform' : itemform, 'item' : item}
        return render(request, 'shopping/edit_model.html', context)
    
