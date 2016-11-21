#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from LifeGame.logic import GameL
from LifeGame.utils import Tools
from django.views.decorators.csrf import csrf_exempt

# ##暂时先都使用get请求
@csrf_exempt
def test(request):
    print("TEST")
    # 获取参数
    row_s = request.GET.get('row', '')
    col_s = request.GET.get('col', '')
    type_s = request.GET.get('type', '')
    result = GameL.test(row_s, col_s, type_s)
    resp = HttpResponse(result)
    resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
    return resp

###############################以上为测试内容

# 游戏设置//1-ok,0-not
@csrf_exempt
def gameSetting(request):
    print("SETTING")
    # 获取参数
    row = Tools.num(request.GET.get('row', '0'))
    col = Tools.num(request.GET.get('col', '0'))
    state = 1;
    if row == 0 or col == 0:
        state = 0;
    if state != 0:
        request.session['row'] = row
        request.session['col'] = col
    resp = HttpResponse(str(state))
    resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
    return resp

# 开始游戏//json-ok,0-not
@csrf_exempt
def gameStart(request):
    print("START")
    # 暂时允许无cookie访问
    row = 0
    col = 0
    try:
        row = request.session['row']
        col = request.session['col']
    except:
        row = 5
        col = 5
    state = "1";
    if row == None or col == None or row == 0 or col == 0:
        state = "0";
    if state != "0":
        data = GameL.getFirstMap(row, col)
        request.session['data'] = data
        state = GameL.getMapJson(data, row, col)
    resp = HttpResponse(state)
    resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
    return resp

# 游戏刷新
@csrf_exempt
def gameRefresh(request):
    print("REFRESH")
    try:
        row = request.session['row']
    except:
        return gameStart(request)
    row = request.session['row']
    col = request.session['col']
    data = request.session['data']
    state = "1";
    if row == None or col == None or row == 0 or col == 0 or data == None:
        state = "0"
    if state != "0":
        data = GameL.getNextMap(data, row, col)
        request.session['data'] = data
        state = GameL.getMapJson(data, row, col)
    print(data)
    resp = HttpResponse(state)
    resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
    return resp


