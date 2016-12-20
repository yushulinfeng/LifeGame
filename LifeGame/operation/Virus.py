#! /usr/bin/env python
# -*- coding: utf-8 -*-


# virus类
#------------------------------------
# 当格子上为virus时进入此类
# 周围没有其他物种则死亡
# 周围Human大于等于6个也会死亡
#------------------------------------
import StaticVar


# 计算是否存活
def IsStillLive(gameMap, xLocation, yLocation):
    otherNumber = CalOtherNumber(gameMap, xLocation, yLocation)
    if otherNumber >= StaticVar.virusminlive and otherNumber < StaticVar.virusmaxlive:
        return True
    return False


# 计算周围的其他物种数
def CalOtherNumber(gameMap, xLocation, yLocation):
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
