from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from .forms import SignupForm
from .models import Fruits

def veg(request):
    return render(request,'veg.html')

def About(request):
    return render(request,'About.html')

def contact(request):
    return render(request,'contact.html')

def signup(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return render(request,"signin.html")
    else:
        fm=SignupForm()
    return render(request,"signup.html",{'form':fm})

def signin(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return render(request, 'profile.html')

    else:
        fm = AuthenticationForm()
    return render(request,"signin.html",{'form':fm})

def signout(request):
    logout(request)
    return render(request,"veg.html")
def profile(request):
    pass

def fruits(request):
    fruits=Fruits.objects.all()
    return render(request,"fruits.html",{'fruits':fruits})
# Create your views here.
