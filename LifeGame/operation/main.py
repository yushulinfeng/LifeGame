#! /usr/bin/env python
# -*- coding: utf-8 -*-
import StaticVar, Human, Virus, Null
import copy

# 后台调用的入口程序
def gameMapAdd(gameMap, xLocation, yLocation, stirps, turn):
    gameMap = AddTogameMap(gameMap, xLocation, yLocation, stirps)
    if CanCalc(turn):
        gameMap = Calculate(gameMap)
    return gameMap


def gameMapWin(gameMap, turn):  # return -2,-1,1,2
    if turn >= 30:
        return CalNumber(gameMap)
    else:
        return WhichDie(gameMap)

# 判断是否需要计算
def CanCalc(turn):
    if turn < StaticVar.prepare or turn % StaticVar.everyCalTurn != 0:
        return False
    else:
        return True

# 将点加入地图中
def AddTogameMap(gameMap, xLocation, yLocation, stirps):
    gameMap[xLocation][yLocation] = stirps
    return gameMap

# 进行生命活动运算
def Calculate(gameMap):
    newgameMap = copy.copy(gameMap)
    for i in range(0, StaticVar.size):
        for j in range(0, StaticVar.size):
            # 当该点为Human的时候
            if gameMap[i][j] == StaticVar.human:
                result = Human.IsToBeVirus(gameMap, i, j)
                if result == True:
                    newgameMap[i][j] = StaticVar.virus
                else:
                    result = Human.IsStillLive(gameMap, i, j)
                    if result == True:
                        pass
                    else:
                        newgameMap[i][j] = StaticVar.null
            # 当该点为Virus的时候
            elif gameMap[i][j] == StaticVar.virus:
                result = Virus.IsStillLive(gameMap, i, j)
                if result == True:
                    pass
                else:
                    newgameMap[i][j] = StaticVar.null
            # 当该点为空的时候
            elif gameMap[i][j] == StaticVar.null:
                newgameMap[i][j] = Null.Born(gameMap, i, j)
    return newgameMap

# 计算数量
def CalNumber(gameMap):
    humancount = 0;
    viruscount = 0;
    for i in range(0, StaticVar.size):
        for j in range(0, StaticVar.size):
            if gameMap[i][j] == StaticVar.human:
                humancount += 1
            elif gameMap[i][j] == StaticVar.virus:
                viruscount += 1
    if humancount > viruscount:
        return StaticVar.human
    elif viruscount > humancount:
        return StaticVar.virus
    else:
        return StaticVar.draw

# 计算是否有一方死亡
def WhichDie(gameMap):
    humancount = 0;
    viruscount = 0;
    for i in range(0, StaticVar.size):
        for j in range(0, StaticVar.size):
            if gameMap[i][j] == StaticVar.human:
                humancount += 1
            elif gameMap[i][j] == StaticVar.virus:
                viruscount += 1
    if humancount == 0 and viruscount > 0:
        return StaticVar.human
    elif viruscount == 0 and humancount > 0:
        return StaticVar.virus
    elif humancount == 0 and viruscount == 0:
        return StaticVar.draw
    else:
        return StaticVar.notfinished
