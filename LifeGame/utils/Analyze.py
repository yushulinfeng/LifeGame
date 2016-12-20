#!/usr/bin/python
# -*- coding: utf-8 -*-

'''性能分析类'''

from LifeGame.logic import GameL
import doctest
import cProfile

def getNextElement(l, x, y, row, col):
    '''
             获取某个点下一次是否是活的生命。
             （测试数据中，第一个是对的，第二个是错的）
    >>> getNextElement([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 1, 3, 3)
    0
    >>> getNextElement([[0, 0, 0], [0, 1, 0], [0, 1, 0]], 1, 1, 3, 3)
    0
    '''
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

# 模拟10x10地图的生命游戏服务器逻辑算法
def logicAnalize():
    row = 10
    col = 10
    data = GameL.getFirstMap(row, col)
    GameL.getMapJson(data, row, col)
    for i in range(0, 20):
        data = GameL.getNextMap(data, row, col)
        GameL.getMapJson(data, row, col)

if __name__ == '__main__':
    print ("START")
    # 命令，二进制输出文件，排序列
    cProfile.run('logicAnalize()', None, 'cumtime')
    # 调用次数（总次数/原生次数），总时间，每次平均时间，之前所有子函数消耗时间的累积和，函数与文件
    print("-"*40)
    doctest.testmod()
    print ("END")
