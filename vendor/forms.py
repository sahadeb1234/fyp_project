from django import forms
from app.models import Product
from app.models import Category

class productaddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','slug', 'category', 'image', 'marked_price', 'selling_price', 'description', 'full_description', 'warranty', 'return_policy', 'view_count','Vendor_name']
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



