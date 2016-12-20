#!/usr/bin/python
# -*- coding: utf-8 -*-

######最最简化
# 初始化（在创建room时，存入）
# 添加，种类，回合数（用户每次操作时，处理，10回合后，开始计算）
# 胜负（30回合时，区分胜负）

####逻辑问题：1/2在对方看来，应该是2/1。
# 即使用您/对手思路时，不同的人看到的地图，应该是1/2版或2/1取决于是哪位用户
# 这个后期replace处理，1->9,2->1,9->2(暂时使用兑数)

import copy

# 行和列数，防止重名
m_r = 30
m_c = 30

def mapInit():
    return [[0 for i in range(m_r)] for i in range(m_c)]  # 全部为0

def mapAdd(m, x, y, t, time=0):  # 位置，类型
    if x < 0  or  x >= m_r  or y < 0 or  y > m_c :
        return m
    m[x][y] = t
    if time == 10 or time == 15 or time == 20 or time == 25:  # 仅在第10,15,20,25回合执行运算
        print("HELLO")
        return dealMap(m)
    return m

def mapWin(m, time=30):  # (time回合数) 0无，1/2有一方胜利，3平局
    if time < 10:  # 前10局不判断
        return 0
    count1 = 0
    count2 = 0
    for x in range(m_r):
        for y in range(m_c):
            if m[x][y] == 1:
                count1 += 1
            if m[x][y] == 2:
                count2 += 1
    if count1 == 0:
        return -2
    if count2 == 0:
        return -1
    if time >= 30 :
        if count1 > count2 :
            return -1
        elif count1 < count2 :
            return -2
        else :
            return -3
    return 0

# 运算方法
def dealMap(l):
    k = [[0 for i in range(m_r)] for i in range(m_c)]  # 下一个0-1界面矩阵
    for x in range(m_r):
        for y in range(m_c):
            m = dealElement(l, x, y)
            if m == 2:
                k[x][y] = l[x][y]
            elif m == 3:
                k[x][y] = 1
            else:
                k[x][y] = 0
    l = copy.deepcopy(k)
    return l

def dealElement(l, x, y):
    m = 0
    for i in (x - 1, x, x + 1):
        for j in (y - 1, y, y + 1):
            if i == x and y == j:
                continue
            if (i < 0 or i > m_r - 1 or j < 0 or j > m_c - 1):
                continue
            if (l[i][j]):
                m += 1
    return m
# 辅助方法
def mapToStr(m):  # 仅包含map，不含其它信息。目前直接一个一维数组字符串即可
    res = ""
    for x in range(m_r):
        for y in range(m_c):
            if x != 0 or y != 0 :
                res += ","
            res += str(m[x][y])
    return res

def strToMap(s):
    m = mapInit()
    try:
        a = s.split(',')
        for i in range(len(a)) :
            m[int(i / m_r)][int(i % m_r)] = int(a[i])
    except:
        pass
    return m

def userChange(s):  # if(user2==tokenId)
    return s.replace('1', '9').replace('2', '1').replace('9', '2')

