from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

# ===================== Login ============================
def login(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        user_pass = request.POST.get("password")
        
        user = auth.authenticate(username = user_name , password = user_pass)
        
        if user is not None:
            return redirect("todo")
        else:
            return redirect("home")
        
    return render(request,"accounts/login.html")

# ===================== Register =========================
def register(request):
    if request.method=="POST":
        user_name = request.POST.get("username")
        user_pass = request.POST.get("password")
        user_conf_pass = request.POST.get("confirm_password")
        
        if user_conf_pass == user_pass:
        
            new_user = User(
                username = user_name
            )
            
            new_user.set_password("user_pass")
            new_user.save()
            
            return redirect("login")
        
        else:
            
            
            return render(request,"accounts/register.html")
        
    return render(request,"accounts/register.html")