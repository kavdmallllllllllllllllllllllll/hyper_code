from django.shortcuts import render
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from.models import cluns ,massgee, images
# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import *
from django.contrib.auth.forms import UserChangeForm

from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def home (request):
    imagess=images.objects.all()
    return render(request,'index.html',{'images':imagess})



def loginn(request ):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username)
        print(password)

        if user is not None:
            
            login(request,user)
            #('profile', user_form.username)
            #'userone' ,jopusers.slug 
            return redirect('profil')
        else:
            messages.success(request,"هناك خطئ في التسجيل تاكد من البيانات وحاول مرة اخري")
            return render (request,'erorr.html')
    return render (request,'login.html')




def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('profil')
        else:
            return render(request, 'signup.html', {'form': form})


def profil(request ):
    clunss=cluns.objects.all()

    
    return render(request,'profil.html',{'cluns':clunss})

def login_out(request ):
    logout(request)
    return redirect('login')

def contact(request):
    if request.method=="POST":
        name= request.POST['name']
        phon= request.POST['phon']
        email= request.POST['email']
        massge= request.POST['massge']
        s=massgee(name=name,phon=phon,email=email,massge=massge)
        s.save()
        k=str('  هناك طلب تواصل من ')
        send_mail(
            k+ str( name ) +str(' تواصل معه علي ')+ str(phon),
            str(massge),

            str(phon),


            ['ka6051152@gmail.com'],
            fail_silently=True


            )


        messages.success(request,"تم ارسال رسالتك بنجاح شكرا لك"   )
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')

