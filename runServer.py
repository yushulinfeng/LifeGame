#!/usr/bin/python
# -*- coding: utf-8 -*-

'''快速启动服务器，允许全部IP访问'''

import os

if __name__ == "__main__":
    doing = "python manage.py runserver 0.0.0.0:8000"
    print ("执行命令：" + doing + "\n")
    os.system(doing)
    print ("执行结束")
 
