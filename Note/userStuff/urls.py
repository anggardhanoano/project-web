from django.urls import path
from userStuff.views import *

app_name = "user"

urlpatterns = [
    path("signup", signup, name = "signup"),
    
    
]

