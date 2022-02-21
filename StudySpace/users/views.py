from dataclasses import fields
from email import message
from django.shortcuts import render,redirect
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
            form=UserRegisterForm()
    return render(request,'users/sign-up.html',{'form':form})
