from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import  TemplateView
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView,TemplateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth  import get_user_model

def error_404(request):
        
        return render(request,'error_404.html')

def error_500(request):
        
        return render(request,'error_500.html')