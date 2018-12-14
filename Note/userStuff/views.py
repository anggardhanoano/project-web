from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import  TemplateView
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView,TemplateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from userStuff.forms import *
from userStuff.models import *
from django.contrib import messages
# Create your views here.




def signup(request) :
    registered = False
    
    if request.method == "POST":
        sign_up = UserForm(data = request.POST)
        print(sign_up) # debugging

        if sign_up.is_valid() :
            user = sign_up.save()   # save to the database
            user.set_password(user.password) # hash the password
            user.save()
            return HttpResponseRedirect(reverse("home"))


        else :
            print(sign_up.errors)
    else :
        sign_up = UserForm()

    
    return render(request, "signup.html", {
                    "sign_up" : sign_up,
                    "title" : "My Note"
    })


def user_login(request) :
    global name
    if request.method == "POST" :
        username = request.POST.get("username")     # grab the input from the user
        password = request.POST.get("password")

        if username == "" or password == "" :
            messages.warning(request, "Please Input Your Username and Password")
            return HttpResponseRedirect(reverse("user_login"))
        else :
            user = authenticate(username = username, password = password)   # return true if username and pass verified
        
            if user :
                if user.is_active :
                    login(request, user)
                    name = request.user
                    
                    return HttpResponseRedirect(reverse("home")) 
                else :
                    messages.warning(request, "Invalid username or password")
                    return HttpResponse("the username or password are invalid")
            else :
                print("there any user failed login")
                print("username: {} and pass: {}".format(username,password))
                messages.warning(request, "Invalid username or password")
                return HttpResponseRedirect(reverse("user_login"))

    else :
        return render(request, "login.html")




@login_required
def user_logout(request) :
    logout(request)
    return HttpResponseRedirect(reverse("user:signup"))



