from django.shortcuts import render
from django.http import HttpResponse
from .models import food_table
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