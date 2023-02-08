from django.shortcuts import render
from django.http import HttpResponse
from food.models import food_table

# Create your views here.

def details(request,lst_int):
    Item=food_table.objects.get(pk=lst_int)
    Context={
        'Item' : Item
    }
    return render(request,'room/details.html',Context)
    # return HttpResponse('12345')

def index(request):
    # Item=food_table.objects.get(pk=listing_id)
    # Context={
    #     'Item' : Item
    # }
    # return render(request,'room/details.html',Context)
    return HttpResponse('1234')
