from django import forms
from django.forms import ModelForm
from userStuff.models import *


class UserForm(forms.ModelForm) :
        username = forms.CharField(label = "",widget=forms.TextInput(
        attrs = {
                "id" : "user",
                "class" : "form-control",
                "placeholder" : "Username",            
                }
    ))
        
        
        password = forms.CharField(label = "",widget=forms.PasswordInput(
                attrs = {
                "id" : "pass",
                "class" : "form-control",
                "placeholder" : "Password",            
                }
        ))
        
        
        email = forms.EmailField(label="",widget=forms.TextInput(
        attrs = {
                "id" : "email",
                "class" : "form-control",
                "placeholder" : "Your Email Adress",           
                }
    ))

        first_name = forms.CharField(label = "", widget=forms.TextInput(
        attrs = {
                "id" : "first",
                "class" : "form-control",
                "placeholder" : "First Name",           
                }
                ))

        last_name = forms.CharField(label = "", widget=forms.TextInput(
        attrs = {
                "id" : "last",
                "class" : "form-control",
                "placeholder" : "Last Name",           
                }
                ))

        class Meta :
                model = User
                fields = ("username", "email", "password","first_name", "last_name")



