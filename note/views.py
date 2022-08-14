from django.shortcuts import render
from django.http import *

# Create your views here.
from note.models import Note


# 登录验证
def checklogin(func):
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'id' not in request.session:
            return HttpResponse('请登录后操作')
        return func(request, *args, **kwargs)

    return wrap


@checklogin
def index(request):
    # 获取笔记列表
    id = request.session['id']
    notes = Note.objects.filter(user_id=id)
    return render(request, 'note/index.html', locals())


@checklogin
def add(request):
    id = request.session['id']
    if request.method == 'GET':
        return render(request, 'note/add.html', locals())
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        # 判断内容与标题是否为空
        if not title or not content:
            return HttpResponse('标题与内容不能为空哦')
        # 将内容写入数据库
        Note.objects.create(title=title, content=content, user_id=id)
        return HttpResponseRedirect('/note')


@checklogin
def mod(request):
    # 获取需要修改的文章ID
    id = request.GET['id']
    note = Note.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'note/mod.html', locals())
    elif request.method == 'POST':
        # 获取前端修改的信息
        title = request.POST['title']
        content = request.POST['content']
        # 判断文章标题与内容是否为空
        if not content or not title:
            return HttpResponse('文章标题与内容不能为空')
        # 更新数据进数据库
        note.title = title
        note.content = content
        note.save()
        # 返回文章列表
        return HttpResponseRedirect('/note/')


def delete(request, id):
    try:
        note = Note.objects.get(id=id)
        note.delete()
        return HttpResponseRedirect('/note')
    except:
        return HttpResponse('删除文章失败')
