#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from LifeGame.logic import GameL, RoomL, FriendL
from LifeGame.models import Token, Room
from LifeGame.utils import Tools
from django.views.decorators.csrf import csrf_exempt

####暂时不处理种族了，太麻烦了

# tokenId获取。此方法为内部方法。
def getTokenId(request):
    # 优先使用用户上传的，此处不必进行session与数据库处理
    token_id = request.GET.get('token', None)
    if (token_id != None) and (token_id != ""):
        return token_id;
    # 用户没有上传token
    token_id = request.session.get('token', None)
    if token_id == None:
        token_id = Token.getNewToken()
        request.session['token'] = token_id  # 没有set方法
    # 数据库处理
    db = Token.objects.filter(tokenId=token_id)
    if len(db) == 0:
        db = Token(tokenId=token_id)
        try:
            db.save()
        except:  # 此处的异常不必处理
            print("TOKEN_SAVE_ERROR")
    return token_id

# token对象获取
def getToken(tokenId):
    db = Token.objects.filter(tokenId=tokenId)
    if len(db) == 0:
        return None
    for t in db:
        return t
    return None

# room对象获取
def getRoom(roomId):
    db = Room.objects.filter(roomId=roomId)
    if len(db) == 0:
        return None
    for t in db:
        return t
    return None

# token获取。此处使用会话进行缓存，并添加至数据库。
@csrf_exempt
def tokenGet(request):
    token_id = getTokenId(request)
    resp = HttpResponse(token_id)
    resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
    return resp

# 对手匹配
# 0等待，1匹配成功
@csrf_exempt
def matchFriend(request):
    token_id = getTokenId(request)
    RoomL.cleanRoom(token_id)
    wait = False
    roomId = RoomL.gotoOneRoom(token_id)
    if roomId == None:
        wait = True
        roomId = RoomL.createRoom(token_id)
    RoomL.dealRoomToken(roomId, token_id)
    resp = HttpResponse("0" if wait else "1")
    resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
    return resp

# 对手匹配状态查询
# 0等待，1匹配成功
@csrf_exempt
def matchState(request):
    token_id = getTokenId(request)
    wait = RoomL.checkInRoom(token_id)
    resp = HttpResponse("0" if (wait == None) else "1")
    resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
    return resp

# 游戏状态
@csrf_exempt
def gameState(request):
    token_id = getTokenId(request)
    token = getToken(token_id)
    if token == None: return errorResp()
    room = getRoom(token.roomId)
    if room == None: return errorResp()
    # #获取数据，执行运算
    ctrl = (room.turnCount % 2 == 0 and room.user2 == token_id)\
            or (room.turnCount % 2 == 1 and room.user1 == token_id)
    state = 1 if ctrl else 2
    t = 1 if room.user1 == token_id else 2
    m_str = room.info
    if(t == 2):
        m_str = FriendL.userChange(m_str)
    win = FriendL.mapWin(FriendL.strToMap(room.info), room.turnCount)
    if(win != 0):
        state = win
    res = "{\"state\":" + str(state) + ",\"type\":" + "1" + \
    ",\"r\":30,\"c\":30" + ",\"d\":[" \
    + m_str + "]}"
#     + ",\"zu\":" + "[1,2,3]" + "}"
    # #处理数据并进行返回
    resp = HttpResponse(res)
    resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
    return resp

# 游戏操作
# 0操作失败，gameState操作成功
@csrf_exempt
def gameUpload(request):
    token_id = getTokenId(request)
    token = getToken(token_id)
    if token == None: return errorResp()
    room = getRoom(token.roomId)
    if room == None: return errorResp()
#     t = request.GET.get('type', '')
    # 没有控制权，或者type不合理
    ctrl = (room.turnCount % 2 == 0 and room.user2 == token_id)\
            or (room.turnCount % 2 == 1 and room.user1 == token_id)
    if not ctrl :  # or(t != '1')or(t != '2'):
        resp = HttpResponse("0")
        resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
        return resp
#     # 种族
#     if t == '1':
#         zu = request.GET.get('zu', '')
#         pass  # 执行运算
#     # 添加生命
#     elif t == '2':
#         x = request.GET.get('x', '')
#         y = request.GET.get('y', '')
#         pass  # 执行运算
    # 目前仅可以添加生命
    x = request.GET.get('x', -1)
    y = request.GET.get('y', -1)
    m = FriendL.strToMap(room.info)
    t = 1 if room.user1 == token_id else 2
    FriendL.mapAdd(m, int(x), int(y), t, room.turnCount)
    m_str = FriendL.mapToStr(m)
    room.info = m_str
    # 控制权轮转（即使是上面操作失败了）
    room.turnCount = room.turnCount + 1
    ######暂不添加随机元素
    try:
        room.save()
    except:  # 此处的异常不必处理
        pass
    return gameState(request) 

def errorResp():
    resp = HttpResponse("0")
    resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
    return resp
