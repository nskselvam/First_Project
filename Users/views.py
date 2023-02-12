from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth.decorators import  login_required

# Create your views here.
def register(request):
  
    # return HttpResponse('hi')
  # # form=UserCreationForm()
  
    if request.method == 'POST':
     form = RegisterForm(request.POST)    
     if form.is_valid():
       form.save()
       username=form.cleaned_data.get('username')
       print(username)
       messages.success(request,f'Welcom {username}, Your Account')
       return redirect('food:index')
    else:
       form=RegisterForm()
    return render(request,'Users/register.html',{'form':form})
@login_required
def profilepage(request):
   return render(request,'Users/profile.html')