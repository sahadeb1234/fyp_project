
from tempfile import mktemp
from unicodedata import category
from django import views
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
import random
from .forms import  productaddForm
from app.models import Product
from app.models import Category
from app.models import Order
from django.shortcuts import redirect
from .forms import *
from .models import Resume
from .forms import ResumeForm
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.


# def success(request):
    # vendor = request.PreRegistration.vendor
    # Product = vendor.Product.all()
    # Order = vendor.Order.all()
    # for order in Order:
    #     Order.vendor_amount = 0
    #     Order.vendor_paid_amount = 0
    #     Order.fully_paid = True

    #     for item in Order.items.all():
    #         if item.vendor == request.PreRegistration.vendor:
    #             if item.vendor_paid:
    #                 order.vendor_paid_amount += item.get_total_price()
    #             else:
    #                 order.vendor_amount += item.get_total_price()
    #                 order.fully_paid = False
    # , {'vendor': vendor, 'products': Product, 'orders': Order}
    #    product = Product.objects.filter(user=request.user)
       
       
    #    count = len(product)
    
    #    order = Order.objects.all()
    #    order = order.count()
    #    print(product)
    #    return render(request,'app/vendor/success.html', {'products':product, 'count':count,'orders':order})


    


@login_required
def addshow(request):
    if request.method == 'POST':
        print(request.user)
        fm = productaddForm(request.POST, request.FILES) 

        if fm.is_valid():
             
         te =fm.cleaned_data['title']
         sg =fm.cleaned_data['slug']
         cy =fm.cleaned_data['category']
         ie =fm.cleaned_data['image']
         mk =fm.cleaned_data['marked_price']
         sp =fm.cleaned_data['selling_price']
         de =fm.cleaned_data['description']
         fd =fm.cleaned_data['full_description']
         w =fm.cleaned_data['warranty']
         rp =fm.cleaned_data['return_policy']
         v =fm.cleaned_data['view_count']
         ve =fm.cleaned_data['Vendor_name']
         reg = Product(title=te,slug=sg,category=cy, image=ie,marked_price=mk, selling_price=sp,description=de, full_description=fd,warranty=w,return_policy=rp,view_count=v, Vendor_name=ve,user=request.user.username)
         reg.save()
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



        
 
# @login_required
# def image(request):
#     if request.method == 'POST':
#         print(request.user)
#         fm = PdForm(request.POST, request.FILES) 

#         if fm.is_valid():
             
#          te =fm.cleaned_data['product']
#          sg =fm.cleaned_data['image']
         
#          reg = Product(product=te,image=sg,user=request.user.username)
#          reg.save()
#     else:
#         fm = productaddForm()
#         # ecom = Product.objects.all()
   
#     return render(request, 'app/vendor/add.html', {'form':fm})
             


# class HomeView(View):
#     def get(self, request):
#         form = ResumeForm()
#         return render(request, 'app/vendor/resume.html', {'form':form})



# def post(self, request):
#   form = ResumeForm(request.POST, request.FILES)
#   if form.is_valid():
#    form.save()
#    return render(request,  'app/vendor/resume.html', {'form':form})

# class CandidateView(View):
#  def get(self, request, pk):
#   candidate = Resume.objects.get(pk=pk)
#   return render(request, 'app/vendor/candidate.html', {'candidate':candidate})



# def adbus(request):
#  if request.method == 'POST':
#   fm = ResumeForm(request.POST, request.FILES)
#   if fm.is_valid():
#       fm.save()
#   else:
#       fm = ResumeForm()
#       return render(request, 'app/vendor/resume.html', {'form':fm})
        


  
def adbus(request):
    if request.method == 'POST':
        print(request.user)
        fm = ResumeForm(request.POST, request.FILES) 

        if fm.is_valid():
             
         te =fm.cleaned_data['companyName']
         sg =fm.cleaned_data['company_register_number']
         cy =fm.cleaned_data['state']
         ie =fm.cleaned_data['address']
         me =fm.cleaned_data['mobile']
         mk =fm.cleaned_data['email']
         sp =fm.cleaned_data['businesstype']
         pf =fm.cleaned_data['profile_image']
         de =fm.cleaned_data['company_register_document']
         reg = Resume(companyName=te,company_register_number=sg,state=cy, address=ie,mobile=me, email=mk,businesstype=sp, profile_image=pf,company_register_document=de)
         reg.save()
    else:
        fm = ResumeForm()
        # ecom = Product.objects.all()
   
    return render(request, 'app/vendor/resume.html', {'form':fm})



