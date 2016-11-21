#!/usr/bin/python
# -*- coding: utf-8 -*-

'''工具总类'''

# 其他工具方法在此处配置
from LifeGame.utils.ToolUnzip import unzip
from LifeGame.utils.ToolFile import delFile,lookFile,lookHtmlFile,lookAllFile,lookWebFile

# str->int
def num(string, default=0):
    val = default
    try:
        val = int(string)
    except:
        val = default
    return val



