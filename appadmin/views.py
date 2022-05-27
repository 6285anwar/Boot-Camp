#from email import message
#from pyexpat.errors import messages
#import re
#from django.forms import forms 
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
#from django.contrib.auth.decorators import login_required
#from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
# from .forms import *

# Create your views here.
def dashbord(request): 
    return render(request,'dashbord.html')

def loginpage(request): 
    return render(request,'adminpage.html')

def signuppage(request): 
    return render(request,'adminsign.html')

def signup(request):
    if request.method=='POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirpassword=request.POST['cpassword']

        if password==confirpassword:
            if User.objects.filter(username=username):
                return redirect('signuppage')
            else:
                user=User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                user.save()
                return redirect('loginpage')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashbord')

        else:
            return redirect('loginpage')   







def platform1(request): 
    return render(request,'platform.html')

def platformadd(request): 
    return render(request,'platformadd.html')

def register(request):
    if request.method=="POST":
        p_name=request.POST["pname"]
        p_dsp=request.POST["pdsp"]

        platforms=platform(platformname=p_name, platformdsp=p_dsp)
        platforms.save()
        # courcenames=request.POST['cname']
        # platforms=platform.objects.get(platformname=p_name)
        # pcources=cource(courcenames=courcenames, platformid=platforms)
        # pcources.save()


        return redirect('show')
    else:
        return redirect('platformadd')

def show(request):
    platforms=platform.objects.all()
    return render(request, 'platform.html', {'platform':platforms})


def platformedit(request, platformid):
    platforms=platform.objects.get(platformid=platformid)
    
    return render(request,'platformedit.html', {'platform':platforms})

def update(request, platformid):
    try:
        if request.method=="POST":
            platforms=platform.objects.get(platformid=platformid)
            platforms.platformname=request.POST.get('pname',)
            platforms.platformdsp=request.POST.get('pdsp')
            platforms.save()
            pcources=request.POST['cname']
            pcources=cource.objects.get(platformid=platformid)
            pcources.courcenames=request.POST.get('cname')
            pcources.save()
            return redirect('show')
    except:
        return redirect('platformadd')



def delete(request, platformid):
    platforms=platform.objects.get(platformid=platformid)
    platforms.delete()
    return redirect('show')

def cources(request): 
    return render(request,'cource.html')



def courceadd(request): 
    platforms=platform.objects.all()
    return render(request,'courceadd.html', {"platform":platforms})

def register2(request):
    if request.method=="POST":
        c_name=request.POST["cname"]
        c_dsp=request.POST["cdsp"]
        c_mod=request.POST["cmod"]
        c_level=request.POST["clevel"]
        c_id=request.POST["pname"]

        platforms=platform.objects.get(platformname=c_id)
        cadd=cource(courcenames=c_name, coursedsp=c_dsp, coursemodules=c_mod, courselevel=c_level, platformid=platforms)
        cadd.save()

        


        return redirect('cshow')
    else:
        return redirect('courceadd')

def cshow(request):
    cadd=cource.objects.all()
    return render(request, 'cource.html', {'cource':cadd})


def deletecource(request,  courceid):
    cadd=cource.objects.get( courceid= courceid)
    cadd.delete()
    return redirect('cshow')

def courceedit(request, courceid):
    cedit=cource.objects.get(courceid=courceid)
    return render(request,'courceedit.html', {'cource':cedit})

def update2(request, courceid):
    
    if request.method=="POST":
        cadd=platform.objects.get(courceid=platform)
        cadd.courcenames=request.POST.get('cname',)
        cadd.courcedsp=request.POST.get('cdsp')
        cadd.courcemodules=request.POST.get('cmod')
        cadd.courcelevel=request.POST.get('clevel')

        # platforms=platform.objects.get(platformname=c_id)
        cadd.platform
        cadd.save()

            
        return redirect('cshow')


def tutorials(request):
    tadd=tutorial.objects.all()
    return render(request, 'tutorial.html', {'tutorial':tadd})
   
def tutorialadd(request):
    cadd=cource.objects.all()
    return render(request, 'tutorialadd.html', {"cource": cadd})

def register3(request):
    if request.method=="POST":
        v_name=request.POST["vname"]
        v_dsp=request.POST["vdsp"]
        t_id=request.POST["cname"]
        creg=cource.objects.get(courcenames=t_id)
        try:
            v_video=request.FILES["video1"]
        except:
            v_video='video/video.mp4'
        tadd=tutorial(vedioname=v_name, vediodsp=v_dsp, vedio=v_video, courceid=creg)
        tadd.save()
        
        
        return redirect('tutorials')
    else:
        return redirect('tutorialadd')



def qa(request):
    tadd=tutorial.objects.all()
    return render(request, 'qa.html', {'tutorial':tadd})

def qashow(request):
    qreg=questions.objects.all()
    return render(request, 'qashow.html', {'questions':qreg})

def register4(request):
    if request.method=="POST":
        q_name=request.POST["questionsname"]
        q_answer=request.POST["ans"]
        q_id=request.POST["vname"]
        op1=request.POST["op1"]
        op2=request.POST["op2"]
        op3=request.POST["op3"]
        tadd=tutorial.objects.get(vedioname=q_id)
        qreg=questions(question=q_name,answers=q_answer,tutorialid=tadd, option1=op1, option2=op2, option3=op3 )
        qreg.save()
        
        
        return redirect('qashow')
    else:
        return redirect('qa')

def deleteq(request,  questionsid):
    qreg=questions.objects.get(questionsid= questionsid)
    qreg.delete()
    return redirect('qashow')