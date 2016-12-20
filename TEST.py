#!/usr/bin/python
# -*- coding: utf-8 -*-

'''测试专用'''

import os
import sys
import time
from LifeGame.logic import FriendL
from LifeGame.logic.GameL import test, getNextElement
from LifeGame.utils.Tools import lookHtmlFile
from LifeGame_Server import settings
import cProfile, re
import doctest

def testTest(i):
    '''
    Function to get absolute value of number.
    >>> testTest(1)
    1
    >>> testTest(2)
    2
    >>> testTest(0)
    0
    '''
    return i

if __name__ == '__main__':
    '''测试专用'''
    print ("START")
#     print ("HELLO WORLD")
#     print(test("5", "5", "1"))
#     print(settings.STATIC_ROOT)
#     print(lookHtmlFile(settings.STATIC_ROOT))
#     # 命令，二进制输出文件，排序列
#     cProfile.run('re.compile("foo|bar")', None, 'cumtime')
#     # 调用次数（总次数/原生次数），总时间，每次平均时间，之前所有子函数消耗时间的累积和，函数与文件
#     print(testTest(1))
#     print(getNextElement([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 1, 3, 3))
#     print(getNextElement([[0, 0, 0], [0, 1, 0], [0, 1, 0]], 1, 1, 3, 3))
#     doctest.testmod()
#     import time
#     print(str(time.time()).replace(".",""))
#     m = FriendL.mapInit()
#     m = FriendL.mapAdd(m, 0, 0, 1)
#     m =FriendL.mapAdd(m, 1, 1, 1)
#     m =FriendL.mapAdd(m, 29, 29, 2)
#     print(FriendL.mapWin(m, 30))
#     m =FriendL.mapAdd(m, 28, 28, 3, 9)
#     m =FriendL.mapAdd(m, 28, 28, 3, 10)
#     print(FriendL.mapToStr(m))
#     print(FriendL.userChange(FriendL.mapToStr(m)))
#     print(m)
#     res = "{\"state\":" + "0" + ",\"type\":" + "1" + \
#     ",\"r\":30,\"c\":30" + ",\"d\":[" \
#     + "0,0,0,0" + "]}"
#     print(res)
    print ("END")
