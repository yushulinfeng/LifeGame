#!/usr/bin/python
# -*- coding: utf-8 -*-

'''房间逻辑类'''

from LifeGame.models import Room, Token
from django.db.models.query_utils import Q
from LifeGame.logic import FriendL

# 访问后，直接以您/对方称呼。
# 进行session判断。有session取出ID，否则建立并存入ID，并重置房间号。
# 取房间号，无。有，则保存。

# 需求：
# 1.房间匹配
# 2.获取当前房间的信息（info）
# 3.房间退出


# 匹配对手
# 清理房间的旧数据
def cleanRoom(tokenId):
    db = Room.objects.filter((Q(user1=tokenId) | Q(user2=tokenId)))
    for u in db:  # 登录成功
        try:
            u.delete()
        except:
            pass

def gotoOneRoom(tokenId):  # return roomId/None
    db = Room.objects.filter(state=0)
    for u in db:  # 有单人房间
        u.user2 = tokenId
        u.state = 1
        try:
            u.save()
        except:   
            pass  # 错误不处理
        return u.roomId
    return None

def createRoom(tokenId):  # return roomId
    roomId = Room.getNewRoom()
    db = Room(roomId=roomId, user1=tokenId, info=FriendL.mapToStr(FriendL.mapInit()))
    try:
        db.save()
    except:   
        pass  # 错误不处理
    return roomId

def dealRoomToken(roomId, tokenId): 
    db = Token.objects.filter(tokenId=tokenId)
    for u in db:
        u.roomId = roomId
        try:
            u.save()
        except:
            pass  # 错误不处理

# 查询匹配状态（房间存在且状态为1）(等待状态也返回None)
def checkInRoom(tokenId):  # return roomId/None
    # 必须到ROOM表查询。先查询TOKEN。
    db = Token.objects.filter(tokenId=tokenId)
    for u in db:
        roomId = u.roomId
        if(roomId == None) or (roomId == ""):
            return None
        db_room = Room.objects.filter(roomId=roomId)
        for r in db_room:
            if r.state == 1:
                return roomId
            break
    return None


