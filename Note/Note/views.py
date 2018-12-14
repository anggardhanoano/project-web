from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import  TemplateView
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView,TemplateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth  import get_user_model

def index(request) :
    user = request.user
    if user != "AnonymousUser" :
        return render(request, "home.html")
    else :
        return render(request, "index.html")