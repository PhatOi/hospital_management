# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse
from .EmailBackEnd import EmailBackEnd
from .models import *

# def main(request):
#     template = loader.get_template("main.html")
#     return HttpResponse(template.render())    

def login_page(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect(reverse("admin_home"))
        elif request.user.user_type == '2':
            return redirect(reverse("staff_home"))
        else:
            return redirect(reverse("patient_home"))

    return render(request, 'login.html')

def do_login(request):
    if request.method != "POST":
        return HttpResponse("<h2> Method not allowed </h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect("/admin_home")
            elif user.user_type == "2":
                return HttpResponseRedirect("/staff/staff_home")
            else:
                return HttpResponseRedirect("/patient/patient_home")
        else:
            messages.error(request, "Tài khoản hoặc mật khẩu chưa đúng")
            return HttpResponseRedirect("/")
        

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
