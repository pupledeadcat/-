from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from sympy import false

from myapp.models import SysUser,EventInfo,EmployeeInfo

# Create your views here.

def login(request):
    next_to = request.GET.get('next', false)
    if request.method == "POST":
        userName = request.POST.get("username")
        passWord = request.POST.get("password")
        if SysUser.objects.filter(username=userName,password=passWord).exists():
            request.session['username'] = userName
            user = SysUser.objects.get(username=userName)
            request.session['name'] = user.real_name
            return redirect('/main')
        else:
            return render(request,'login.html',{'message':'用户名/密码错误'})

    return render(request, 'login.html')

def main(request):
    name = request.session.get('name')
    return render(request,'main.html',{'name':name})

def personal(request):
    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        mobile = request.POST.get('mobile')
        user = SysUser.objects.get(username=username)
        user.username = username
        user.real_name = name
        user.email = email
        user.phone = phone
        user.mobile = mobile

        user.save()

    username = request.session.get('username')
    user = SysUser.objects.get(username=username)
    print(user.username)
    return render(request,'personal.html',{'user':user})
def updatepassword(request):
    if request.method == "POST":
        return redirect('/personal')
    return render(request,'updatepassword.html')

def add_old(request):
    if request.method == "POST":
        name = request.POST.get('name')

    name = request.session.get('name')
    return render(request,'add_old.html',{'name':name})