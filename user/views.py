from django.shortcuts import render,redirect
from django.forms import ModelForm
from .models import User,UserManager
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate
# Create your views here.
def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Bạn đã đăng ký thành công!')
            return redirect('main:index')
    else:
            form = RegisterForm()
    return render(request,'user/register.html',{'form':form})
def profile(request):
    
    return render(request,'user/profile.html')
