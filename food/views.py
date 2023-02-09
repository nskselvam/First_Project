from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import food_table
from .forms import Forms_add
# Create your views here.
def index(request):
    Item_data=food_table.objects.all()
    Context={
        'Item_data' : Item_data
    }
    return render(request,'food/index.html',Context)
def first(requst):
    return HttpResponse('Second Html')
def details(request,listing_id):
    Item=food_table.objects.get(pk=listing_id)
    Context={
        'Item' : Item
    }
    return render(request,'food/details.html',Context)

def Adddata(request):
    form=Forms_add(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('food:index')
    print(form)
    return render(request,'food/frm_food_add.html',{'form':form})