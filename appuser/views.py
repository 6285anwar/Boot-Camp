

# Create your views here.

from email import message
from pyexpat.errors import messages
import re
from django.forms import forms 
from django.shortcuts import render, redirect

from appadmin.models import cource

from .models import *
from django.contrib.auth.models import User, auth


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# from .forms import *

from appadmin.models import platform
from appadmin.models import cource,tutorial,questions


from django.contrib.auth import authenticate




# Create your views here.
def userpanel(request):
    
    user=users.objects.get(username=request.session['username'])  
    cources=cource.objects.get(courcenames=user.courcenames)
    # tutorials=tutorial.objects.get(courceid=cources.courceid) 
    return render(request,'userpanel.html',{"users": user,"cource":cources})

def login2page(request): 
    return render(request,'userpage.html')

# def platformselect(request): 
#     platforms=platform.objects.all()
#     return render(request,'register.html',{"platform": platforms})

def signup2page(request): 
    cources=cource.objects.all()
    return render(request,'usersign.html',{"cource": cources})

def signup2(request):
    try:
        if request.method=='POST':
            fname=request.POST['first_name']
            lname=request.POST['last_name']
            uname=request.POST['username']
            uemail=request.POST['email']
            c_name=request.POST["courcename"]
            creg=cource.objects.get(courcenames=c_name)
            upassword=request.POST['password']
            uconfirmpassword=request.POST['cpassword']
            # platform_name=request.POST["platformname"]

            if upassword==uconfirmpassword:
                if users.objects.filter(username=uname):
                    return redirect('login2page')
                else:
                    user=users(firstname=fname, lastname=lname, username=uname, email=uemail, password=upassword, courceid=creg,courcenames=c_name)
                    user.save()
                    return redirect('login2page')
    except:
        return redirect('signup2page')

# def login2(request):
#     if request.method=='POST':
#         uname=request.POST['username']
#         upassword=request.POST['password']
#         user=authenticate(username=uname, password=upassword)
#         if uname==upassword:
#                 if users.objects.filter(uname):
#                     return redirect('userpanel')

#         else:
#             messages.info(request, 'INVALID USERNAME OR PASSWORD')
#             return redirect('login2page')   

# def login2(request):
#     if request.method=='POST':
#             userd=users.objects.get(username=request.POST['username'],password=request.POST['password'])
#             request.session['username']=userd.username
#             return redirect('userpanel')
    
    # else:
    #         messages.info(request, 'INVALID USERNAME OR PASSWORD')
    #         return redirect('login2page') 

def login2(request):
    try:

        if request.method=='POST':
                userd=users.objects.get(username=request.POST['username'],password=request.POST['password'])
                request.session['username']=userd.username
                return redirect('userpanel')
    except users.DoesNotExist as e:
        messages.success(request, 'username or password is invalid')
        return redirect('login2page')



def courcetutorial(request):
    user=users.objects.get(username=request.session['username'])
    cources=cource.objects.get(courcenames=user.courcenames)
    tutorials=tutorial.objects.filter(courceid=cources.courceid) 
    

    return render(request,'courcetutorial.html',{"users": user,"cource":cources,"tutorial":tutorials})


def quiz(request):

    user=users.objects.get(username=request.session['username'])
    cources=cource.objects.get(courcenames=user.courcenames)
    tutorials=tutorial.objects.filter(courceid=cources.courceid)
    exam=questions.objects.filter(tutorialid=tutorials.tutorialid)

    return render(request,'quiz.html',{"users": user,"cource":cources,"tutorial":tutorials,"questions":exam})

def certificate(request):
    user=users.objects.get(username=request.session['username'])
    cources=cource.objects.get(courcenames=user.courcenames)
    return render(request,'cirt.html',{"users": user,"cource":cources})


def download(request):
    return render(request,'download.html')