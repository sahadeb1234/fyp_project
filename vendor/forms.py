from pyexpat import model
from attr import attr, field, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.core import validators
from app.models import Product
from app.models import Category
def validete_username(value):
    if len(value)<=2:
        raise forms.ValidationError(f"Your username cannot be of {len(value)}  word")

class CreateUser(UserCreationForm):
    password1 = forms.CharField(label="Password", widget = forms.PasswordInput(attrs={"placeholder":"Password",'autocomplete':'new-password','class':'form-control'}),error_messages={"required":"Please enter password"},)
    password2 = forms.CharField(label="Re-enter",widget= forms.PasswordInput(attrs={"placeholder":"Re-Enter",'autocomplete':'new-password','class':'form-control'}),help_text="Make sure your password contains 'small letter','capital letter','numbers' and 'symbols'",error_messages={"required":"Re-Enter password field cannot be empty"})
    username = forms.CharField(label="username",widget=forms.TextInput(attrs={"placeholder":"Username","id":"username",'class':'form-control'}),validators=[validete_username])
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name","required":True,'class':'form-control'}),error_messages={"required":"First name cannot be empty"})
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name","required":True,'class':'form-control'}),error_messages={"required":"Last name cannot be empty"})
    email = forms.CharField(widget=forms.EmailInput(attrs={"required":True,"Placeholder":"Email",'class':'form-control'}),error_messages={'required':'Email fields should not be empty'})
    class  Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2']
    

class VerifyForm(forms.Form):
    otp = forms.CharField(label='OTP',max_length=70,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'OTP','required':True}),error_messages={'required':'Enter a otp'})


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"placeholder":"Username","class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password",'autocomplete':'current-password',"class":"form-control"}))  

class productaddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','slug', 'category', 'image', 'marked_price', 'selling_price', 'description', 'full_description', 'warranty', 'return_policy', 'view_count']
        widgets = {
             'title': forms.TextInput(attrs={'class':'form-control'}),
             'slug': forms.TextInput(attrs={'class':'form-control'}),
             'category': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'required': False,'class': 'form-control','enctype': 'multipart/form-data'}),
            'marked_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'full_description': forms.TextInput(attrs={'class':'form-control'}),
            'warranty': forms.TextInput(attrs={'class':'form-control'}),
            'return_policy': forms.TextInput(attrs={'class':'form-control'}),
            'view_count': forms.NumberInput(attrs={'class':'form-control'}),


           

           

          
        }



