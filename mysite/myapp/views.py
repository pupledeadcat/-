import os
import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.timezone import now
from sqlalchemy import null
from sympy import false

from myapp.models import SysUser,EventInfo,EmployeeInfo,OldpersonInfo

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
            request.session['uid'] = user.id
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
# 新增老人信息
def add_old(request):

    name = request.session.get('name')
    if request.method == "POST":
        old_name = request.POST.get('name')
        sex = request.POST.get('sex')
        id_card = request.POST.get('id')
        birthday = request.POST.get('birth')
        health = request.POST.get('health')
        indate = request.POST.get('indate')
        room = request.POST.get('room')
        phone = request.POST.get('phone')

        name1 = request.POST.get('name1')
        relation1 = request.POST.get('relation1')
        phone1 = request.POST.get('phone1')
        wx1 = request.POST.get('wx1')
        name2 = request.POST.get('name2')
        relation2 = request.POST.get('relation2')
        phone2 = request.POST.get('phone2')
        wx2 = request.POST.get('wx2')

        bz = request.POST.get('bz')


        myFile = request.FILES.get("f")  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            message = '请上传头像'

            return render(request, 'add_old.html', {'name': name, 'message': message})
        filename = old_name + room +'jpg'
        path = os.path.join('static/老人头像', filename)
        destination = open(path, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        uid = request.session.get('uid')

        OldpersonInfo.objects.create(username=old_name,gender=sex,phone=phone,profile_photo=filename,
                                     id_card=id_card,birthday=birthday,
                                     health_state=health, checkin_date=indate,
                                     room_number=room,firstguardian_name=name1,
                                     firstguardian_relationship=relation1,
                                     firstguardian_phone=phone1,firstguardian_wechat=wx1,
                                     secondguardian_name=name2,secondguardian_relationship=relation2,
                                     secondguardian_phone=phone2,secondguardian_wechat=wx2,
                                     description=bz, createby=uid,created=now(),remove=0)
        message = '创建成功'

        return render(request, 'add_old.html', {'name': name,'message':message})
    return render(request,'add_old.html',{'name':name})
# 老人信息管理
def olds_info(request):
    name = request.session.get('name')
    olds = OldpersonInfo.objects.filter(remove=0)
    return render(request,'olds_info.html',{'name':name,'olds':olds})
# 查看老人详细信息
def old_detail(request):
    id = request.GET['id']
    old = OldpersonInfo.objects.get(id=id)
    name = request.session.get('name')
    return render(request,'old_detail.html',{'name':name,'old':old})