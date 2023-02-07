from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(retruns):
    return HttpResponse('Frist Html')
def first(retruns):
    return HttpResponse('Second Html')