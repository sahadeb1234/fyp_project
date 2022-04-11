from cProfile import label
from pyexpat import model
from attr import fields
from django import forms
from app.models import Product
from app.models import Category    
from app.models import ProductImage
from .models import Resume

class productaddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','slug', 'category', 'brand', 'storage',  'image', 'marked_price', 'selling_price', 'description', 'full_description', 'warranty', 'return_policy', 'view_count','Vendor_name']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'required': False,'class': 'form-control','enctype': 'multipart/form-data'}),
            'marked_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'full_description': forms.TextInput(attrs={'class':'form-control'}),
            'warranty': forms.TextInput(attrs={'class':'form-control'}),
            'return_policy': forms.TextInput(attrs={'class':'form-control'}),
            'user':forms.TextInput(attrs={'class': 'form-control'}),
            'view_count': forms.NumberInput(attrs={'class':'form-control'}), 
            'Vendor_name': forms.TextInput(attrs={'class':'form-control'}),  
          
          
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'slug']
        widgets ={
             'title': forms.TextInput(attrs={'class':'form-control'}),
              'slug': forms.TextInput(attrs={'class':'form-control'}),


        }

# class PdForm(forms.ModelForm):
#     class Meta:
#         model = ProductImage
#         fields = ['product', 'image']
#         widgets ={
#              'product': forms.TextInput(attrs={'class':'form-control'}),
#               'image': forms.TextInput(attrs={'class':'form-control'}),


#         }



class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['companyName', 'company_register_number', 'state', 'address', 'mobile','email', 'businesstype','profile_image', 'company_register_document']
        widgets = {
             'companyName':forms.TextInput(attrs={'class':'form-control'}),
             'company_register_number':forms.NumberInput(attrs={'class':'form-control'}),
             'state':forms.Select(attrs={'class':'form-select'}),
             'address':forms.TextInput(attrs={'class':'form-control'}),
             'mobile':forms.NumberInput(attrs={'class':'form-control'}),
             'email':forms.EmailInput(attrs={'class':'form-control'}),
             'businesstype':forms.TextInput(attrs={'class':'form-control'}),
             'profile_image': forms.FileInput(attrs={'required': False,'class': 'form-control','enctype': 'multipart/form-data'}),
             'company_register_document': forms.FileInput(attrs={'required': False,'class': 'form-control','enctype': 'multipart/form-data'}),
  
  }
     
        





