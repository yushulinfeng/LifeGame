#! /usr/bin/env python
# -*- coding: utf-8 -*-


# human类
#------------------------------------
# 当格子上为human时进入此类
# 周围有2-5个同类就存活否则就死亡
# 周围有三个病毒则会变成病毒
#------------------------------------
import StaticVar

# 计算是否变异
def IsToBeVirus(gameMap, xLocation, yLocation):
    virusNumber = CalVirusNumber(gameMap, xLocation, yLocation)
    if virusNumber >= StaticVar.humantobevirus:
        return True
    else:
        return False

# 计算是否存活
def IsStillLive(gameMap, xLocation, yLocation):
    humanNumber = CalHumanNumber(gameMap, xLocation, yLocation)
    if humanNumber <= StaticVar.humanmaxlive and humanNumber >= StaticVar.humanminlive:
        return True
    return False


# 计算周围的human数
def CalHumanNumber(gameMap, xLocation, yLocation):
    count = 0
    size = StaticVar.size
    # 左上
    if xLocation - 1 >= 0 and yLocation - 1 >= 0 and gameMap[xLocation - 1][yLocation - 1] == StaticVar.human:
        count += 1
    # 中上
    if yLocation - 1 >= 0 and gameMap[xLocation][yLocation - 1] == StaticVar.human:
        count += 1
    # 右上
    if xLocation + 1 < size and yLocation - 1 >= 0 and gameMap[xLocation + 1][yLocation - 1] == StaticVar.human:
        count += 1
    # 左中
    if xLocation - 1 >= 0  and gameMap[xLocation - 1][yLocation] == StaticVar.human:
        count += 1
    # 右中
    if xLocation + 1 < size and gameMap[xLocation + 1][yLocation] == StaticVar.human:
        count += 1
    # 左下
    if xLocation - 1 >= 0 and yLocation + 1 < size and gameMap[xLocation - 1][yLocation + 1] == StaticVar.human:
        count += 1
    # 中下
    if yLocation + 1 < size and gameMap[xLocation][yLocation + 1] == StaticVar.human:
        count += 1
    # 右下
    if xLocation + 1 < size and yLocation + 1 < size and gameMap[xLocation + 1][yLocation + 1] == StaticVar.human:
        count += 1
    return count

def CalVirusNumber(gameMap, xLocation, yLocation):
    count = 0
    size = StaticVar.size
    # 左上
    if xLocation - 1 >= 0 and yLocation - 1 >= 0 and gameMap[xLocation - 1][yLocation - 1] == StaticVar.virus:
        count += 1
    # 中上
    if yLocation - 1 >= 0 and gameMap[xLocation][yLocation - 1] == StaticVar.virus:
        count += 1
    # 右上
    if xLocation + 1 < size and yLocation - 1 >= 0 and gameMap[xLocation + 1][yLocation - 1] == StaticVar.virus:
        count += 1
    # 左中
    if xLocation - 1 >= 0  and gameMap[xLocation - 1][yLocation] == StaticVar.virus:
        count += 1
    # 右中
    if xLocation + 1 < size and gameMap[xLocation + 1][yLocation] == StaticVar.virus:
        count += 1
    # 左下
    if xLocation - 1 >= 0 and yLocation + 1 < size and gameMap[xLocation - 1][yLocation + 1] == StaticVar.virus:
        count += 1
    # 中下
    if yLocation + 1 < size and gameMap[xLocation][yLocation + 1] == StaticVar.virus:
        count += 1
    # 右下
    if xLocation + 1 < size and yLocation + 1 < size and gameMap[xLocation + 1][yLocation + 1] == StaticVar.virus:
        count += 1
    return count

