#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, time
from LifeGame_Server import settings
from LifeGame.utils import Tools
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# 网页
# 管理员相关，目前仅提供网页管理
def manage(request):
    login = request.session.get('manager', '')
    if login == 'manager':
        root = settings.STATIC_ROOT + '/home'
        host = request.get_host()  # 获取服务器的IP
        return render(request, 'managerHtml.html', {'title': "生命游戏-网站管理", \
                'file_list':Tools.lookWebFile(root, host)})  
    else:
        return render(request, 'managerLogin.html', {'title': "管理员登录"})

# 接口
# 管理员登录，目前仅允许rjgc(软件工程)登录管理
@csrf_exempt  # 禁用csrf检查，否则js-post表单会被拦截
def managerLogin(request):
    username = request.POST.get('name', '')
    password = request.POST.get('pass', '')
    resp = HttpResponse("0")
    if username == 'rjgc' and password == 'rjgc':
        request.session['manager'] = 'manager'
        resp = HttpResponse("1")
    resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
    return resp

# 接口
# 管理HTML网页，上传ZIP压缩包，部署到网页
@csrf_exempt
def managerHtml(request):
    upFile = request.FILES.get('htmlZip', None)
    filePath = settings.STATIC_ROOT + '/manager'  # 最后定义成全局量    #sdoc_raw/sdoc_deal
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    succ = False
    if upFile != None:
        # html_%Y%m%d_%H%M%S.zip
        fileName = 'html_' + \
        time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time())) + '.zip'
        stream = open(filePath + '/' + fileName, 'wb+')
        for chunk in upFile.chunks():
            stream.write(chunk)
        stream.close()
        try:
            fileNewPath = settings.STATIC_ROOT + '/home'
            Tools.delFile(fileNewPath)  # 删除原来的文件
            Tools.unzip(filePath + '/' + fileName, fileNewPath)
            succ = True
        except:
            succ = False
    if succ:
        return render(request, 'managerError.html', {'text': r"提交成功<br/>正在刷新数据", \
                'time':'1', 'url':'manager'})  # 已经在页面中允许不转义
    return render(request, 'managerError.html', {'text': r"提交失败<br/>本页将在3秒后返回", \
                'time':'3', 'url':'manager'})  # 已经在页面中允许不转义
