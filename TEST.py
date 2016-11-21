#!/usr/bin/python
# -*- coding: utf-8 -*-

'''测试专用'''

import os
import sys
import time
from LifeGame.logic.GameL import test
from LifeGame.utils.Tools import lookHtmlFile
from LifeGame_Server import settings
import cProfile, re

if __name__ == '__main__':
    '''测试专用'''
    print ("START")
    print ("HELLO WORLD")
    print(test("5", "5", "1"))
    print(settings.STATIC_ROOT)
    print(lookHtmlFile(settings.STATIC_ROOT))
    # 命令，二进制输出文件，排序列
    cProfile.run('re.compile("foo|bar")', None, 'cumtime')
    #调用次数（总次数/原生次数），总时间，每次平均时间，之前所有子函数消耗时间的累积和，函数与文件
    print ("END")







