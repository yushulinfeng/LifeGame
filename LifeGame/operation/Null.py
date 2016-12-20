#! /usr/bin/env python
# -*- coding: utf-8 -*-
import StaticVar


# Null类
#------------------------------------
# 当格子上为Null时进入此类
# 周围有2-3个human时生成一个human
# 周围不全是virus时生成virus
#------------------------------------

def Born(gameMap, xLocation, yLocation):
    virusNumber = CalVirusNumber(gameMap, xLocation, yLocation)
    humanNumber = CalHumanNumber(gameMap, xLocation, yLocation)
    if virusNumber >= StaticVar.virusminborn and virusNumber < StaticVar.virusmaxborn:
        return StaticVar.virus
    elif humanNumber >= StaticVar.humanminborn and humanNumber <= StaticVar.humanmaxborn:
        return StaticVar.human
    else :
        return StaticVar.null

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
