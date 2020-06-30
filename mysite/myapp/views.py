from django.shortcuts import render, redirect
from myapp import *

# Create your views here.

def login(request):
    if request.method == "POST":
        userName = request.POST.get("username")
        passWord = request.POST.get("password")


    return render(request, 'login.html')
