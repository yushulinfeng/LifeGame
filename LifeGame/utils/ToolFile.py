#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from LifeGame_Server import settings

# 删除非空文件夹
def delFile(src):  
    if os.path.isfile(src):  
        try:  
            os.remove(src)  
        except:  
            pass 
    elif os.path.isdir(src):  
        for item in os.listdir(src):  
            itemsrc = os.path.join(src, item)  
            delFile(itemsrc)  
        try:  
            os.rmdir(src)  
        except:  
            pass 
        
# 查看文件夹
def lookFile(src, arr=None):
    if arr == None:
        arr = []
    if os.path.isfile(src):  
        arr.append(src)  
    elif os.path.isdir(src):  
        for item in os.listdir(src):  
            itemsrc = os.path.join(src, item)  
            lookFile(itemsrc, arr) 
        arr.append(src)  
    return arr

# 查看文件夹
def lookWebFile(src, host='120.27.98.95'):
    arr = lookAllFile(src)
    arr_new = []
    for a in arr:
        ishtml = True
        if not (a.endswith('htm') or a.endswith('html')):
            ishtml = False
        arr_new.append(WebFile(a, ishtml))
    del arr
    return arr_new

# 查看文件夹
def lookHtmlFile(src, host='120.27.98.95'):
    arr = lookAllFile(src)
    # remove()在删除数组单个元素的时候，删完元素很明显需要把指针位置向前移1位，直接for+remove会产生元素跳过
    arr_temp = arr[:]  # arr_temp仅仅是一个指向arr数组的指针而已。  
    for a in arr_temp:  
        if not (a.endswith('htm') or a.endswith('html')):
            arr.remove(a)
    del arr_temp;
    return arr

# 查看文件夹
def lookAllFile(src, host='120.27.98.95'):
    arr = lookFile(src)
    for i in range(0, len(arr)):  # range是包括start但不包括end的
        arr[i] = arr[i].replace(settings.STATIC_ROOT, "http://" + host + "/LifeGame/web")
        arr[i] = arr[i].replace('\\', "/")
    arr.reverse()
    return arr

# 查看文件夹
class WebFile(object):
    def __init__(self, filename, ishtml):   
        self.filename = filename
        self.ishtml = ishtml
        
