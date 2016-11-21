#!/usr/bin/python
# -*- coding: utf-8 -*-

'''游戏逻辑类-总类'''

import random
import copy
# session暂时存储：
# row,col,array（暂时使用一维数组即可）

# 测试专用方法
# 行数，列数，种类数
def test(row_s, col_s, type_s):
    row = 5
    col = 5
    type = 1
    if row_s != '':
        try:
            row = int(row_s)
        except:
            row = 5
    if col_s != '':
        try:
            col = int(col_s)
        except:
            col = 5
    if type_s != '':
        try:
            type = int(type_s)
        except:
            type = 1
    result = "{\"r\":" + str(row) + ",\"c\":" + str(col) + ",\"t\":" + str(type) + ",\"d\":[";
    for i in range(0, row):
        for j in range (0, col):
            value = random.randint(0, type);  # 0-type
            result += str(value);  # 1.0
            if (i != (row - 1) or j != (col - 1)):
                result += ",";
    result += "]}";
    return result

#####直接模拟
def getFirstMap(row, col):
    l = [[random.choice((0, 1)) for i in range(row)] for i in range(col)]  # 当前的0-1界面矩阵
    return l

def getNextMap(l, row, col):
    k = [[0 for i in range(row)] for i in range(col)]  # 下一个0-1界面矩阵
    for x in range(row):
        for y in range(col):
            m = getNextElement(l, x, y, row, col)
            if m == 2:
                k[x][y] = l[x][y]
            elif m == 3:
                k[x][y] = 1
            else:
                k[x][y] = 0
    l = copy.deepcopy(k)
    return l

def getNextElement(l, x, y, row, col):
    m = 0
    for i in (x - 1, x, x + 1):
        for j in (y - 1, y, y + 1):
            if i == x and y == j:
                continue
            if (i < 0 or i > row - 1 or j < 0 or j > col - 1):
                continue
            if (l[i][j]):
                m += 1
    return m

def getMapJson(l, row, col):
    result = "{\"r\":" + str(row) + ",\"c\":" + str(col) + ",\"t\":1,\"d\":[";
    for i in range(0, row):
        for j in range (0, col):
            value = l[i][j];  # 0-type
            result += str(value);  # 1.0
            if (i != (row - 1) or j != (col - 1)):
                result += ",";
    result += "]}";
    return result
    
#######################################以上为测试代码



