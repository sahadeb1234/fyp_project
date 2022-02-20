
from unicodedata import category
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from numpy import delete
from . forms import CreateUser
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
import random
from .models import PreRegistration
from .forms import VerifyForm,LoginForm
from .forms import  productaddForm
from django.contrib.auth import login,logout,authenticate
from app.models import Product
from app.models import Category
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def creatingOTP():
    otp = ""
    for i in range(11):
        otp+= f'{random.randint(0,9)}'
    return otp

def sendEmail(email):
    otp = creatingOTP()
    send_mail(
    'One Time Password',
    f'Your OTP pin is {otp}',
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
    )
    return otp


def createUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                otp = sendEmail(email)
                dt = PreRegistration(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],username= form.cleaned_data['username'],email=email,otp=otp,password1 = form.cleaned_data['password1'],password2 = form.cleaned_data['password2'])
                dt.save()
                return HttpResponseRedirect('/verify/')
                
                
        else:
            form = CreateUser()
        return render(request,"app/vendor/register.html",{'form':form})
    else:
        return HttpResponseRedirect('/success/')

def login_function(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usr = authenticate(username=username,password = password)
                if usr is not None:
                    login(request,usr)
                    return HttpResponseRedirect('/success/')
        else:
            form = LoginForm()
        return render(request,'app/vendor/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/success/')

def verifyUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = VerifyForm(request.POST)
            if form.is_valid():
                otp = form.cleaned_data['otp']
                data = PreRegistration.objects.filter(otp = otp)
                if data:
                    username = ''
                    first_name = ''
                    last_name = ''
                    email = ''
                    password1 = ''
                    for i in data:
                        print(i.username)
                        username = i.username
                        first_name = i.first_name
                        last_name = i.last_name
                        email = i.email
                        password1 = i.password1

                    user = User.objects.create_user(username, email, password1)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    data.delete()
                    messages.success(request,'Account is created successfully!')
                    return HttpResponseRedirect('/verify/')   
                else:
                    messages.success(request,'Entered OTO is wrong')
                    return HttpResponseRedirect('/verify/')
        else:            
            form = VerifyForm()
        return render(request,'app/vendor/verify.html',{'form':form})
    else:
        return HttpResponseRedirect('/success/')


   

def logout_function(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def success(request):
    #  if request.method == 'POST':

    #     fm = productaddForm(request.POST, request.FILES)
    #     if fm.is_valid():
    #      fm.save()
    #     else:
    #         fm = productaddForm()
    #     ecom = Product.objects.all()
        return render(request,'app/vendor/success.html')



@login_required
def addshow(request):
    if request.method == 'POST':

        fm = productaddForm(request.POST, request.FILES)
        if fm.is_valid():
             
        #  te =fm.cleaned_data['title']
        #  sg =fm.cleaned_data['slug']
        #  cy =fm.cleaned_data['category']
        #  ie =fm.cleaned_data['image']
        #  mk =fm.cleaned_data['marked_price']
        #  sp =fm.cleaned_data['selling_price']
        #  de =fm.cleaned_data['description']
        #  fd =fm.cleaned_data['full_description']
        #  w =fm.cleaned_data['warranty']
        #  rp =fm.cleaned_data['return_policy']
        #  v =fm.cleaned_data['view_count']
        #  reg = Product(title=te,slug=sg,category=cy, image=ie,marked_price=mk, selling_price=sp,description=de, full_description=fd,warranty=w,return_policy=rp,view_count=v)
         fm.save()
    else:
        fm = productaddForm()
        # ecom = Product.objects.all()
   
    return render(request, 'app/vendor/add.html', {'form':fm})

@login_required
def Categ(request):
     if request.method == 'POST':
          cat = CategoryForm(request.POST, request.FILES)
          if cat.is_valid():
              cat.save()
     else:
         cat = CategoryForm()
     stu = Category.objects.all()
     return render(request, 'app/vendor/Category.html', {'form':cat, 'stud':stu})

def delete_data(request, id):
    if request.method =='POST':
        Pi = Category.objects.get(pk=id)
        Pi.delete()
        return HttpResponseRedirect('/Category/')

def update(request, id):
    if request.method == 'POST':
        pi = Category.objects.get(pk=id)
        fm = CategoryForm(request.POST, instance=pi)
        if fm.is_valid():
         fm.save()
    else:
        pi = Category.objects.get(pk=id)
        fm = CategoryForm(instance=pi)
    return render(request, 'app/vendor/updatecategory.html', {'form':fm})



        
 

             


