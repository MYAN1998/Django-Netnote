import requests
from django.http import *
from django.shortcuts import render
import hashlib

# Create your views here.
from user.models import User


def login(request):
    if request.method == 'GET':
        if 'username' in request.session and 'id' in request.session:
            return HttpResponseRedirect('/note')
        return render(request, 'user/login.html', locals())
    elif request.method == 'POST':
        # 获取前端的用户名与密码
        username = request.POST['username']
        password = request.POST['password']
        # 判断用户名与密码是否为空
        if not username or not password:
            return HttpResponse('输入的用户名与密码不能为空')
        # 判断用户名是否存在
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('用户名或密码错误')
        # 判断密码是否正确
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        if password_h == user.password:
            # 将登录信息写入session
            request.session['username'] = user.username
            request.session['id'] = user.id
            return HttpResponseRedirect('/note')
        else:
            return HttpResponse('用户名或密码错误')


def reg(request):
    if request.method == 'GET':
        return render(request, 'user/reg.html', locals())
    elif request.method == 'POST':
        # 获取前端数据
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        # 判断用户名与密码是否为空
        if not username or not password_1:
            return HttpResponse('用户名与密码不能为空')
        # 判断用户名是否重复
        try:
            user = User.objects.get(username=username)
            return HttpResponse('用户名已被占用请选择其他用户名')
        except:
            # 判断两次密码是否一致
            if password_1 != password_2:
                return HttpResponse('两次密码不一致')
            # 加密密码
            md5 = hashlib.md5()
            md5.update(password_1.encode())
            password_h = md5.hexdigest()
            # 将数据写入数据库
            User.objects.create(username=username, password=password_h)
            # 跳转至登录界面
            return HttpResponseRedirect('/user/login')


def logout(request, id):
    try:
        user = User.objects.get(id=id)
        del request.session['username']
        del request.session['id']
    except:
        return HttpResponse('退出失败')
    return HttpResponseRedirect('/')
