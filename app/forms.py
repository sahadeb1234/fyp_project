from django import forms
from django.db import models
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User



class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by", "shipping_address",
                  "mobile", "email", "payment_method"]
        widgets = {'ordered_by': forms.TextInput(attrs={'class':'form-control'}), 'shipping_address': forms.TextInput(attrs={'class':'form-control'}), 'mobile': forms.TextInput(attrs={'class':'form-control'}), 'email': forms.TextInput(attrs={'class':'form-control'})}


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","id":"username",'class':'form-control'}))
    password = forms.CharField(label="Password", widget = forms.PasswordInput(attrs={"placeholder":"Password",'autocomplete':'new-password','class':'form-control'}),error_messages={"required":"Please enter password"},)
    email = forms.CharField(widget=forms.EmailInput(attrs={"required":True,"Placeholder":"Email",'class':'form-control'}),error_messages={'required':'Email fields should not be empty'})
    class Meta:
        model = Customer
        fields = ["username", "password", "email", "full_name", "address"]
        widgets = {'full_name': forms.TextInput(attrs={'class':'form-control'}), 'address': forms.TextInput(attrs={'class':'form-control'})}



    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Customer with this username already exists.")

        return uname

class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password",'autocomplete':'current-password',"class":"form-control"}))

class PasswordForgotForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Enter the email used in customer account..."
    }))

    def clean_email(self):
        e = self.cleaned_data.get("email")
        if Customer.objects.filter(user__email=e).exists():
            pass
        else:
            raise forms.ValidationError(
                "Customer with this account does not exists..")
        return e


class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'autocomplete': 'new-password',
        'placeholder': 'Enter New Password',
    }), label="New Password")
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'autocomplete': 'new-password',
        'placeholder': 'Confirm New Password',
    }), label="Confirm New Password")

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        confirm_new_password = self.cleaned_data.get("confirm_new_password")
        if new_password != confirm_new_password:
            raise forms.ValidationError(
                "New Passwords did not match!")
        return confirm_new_password
