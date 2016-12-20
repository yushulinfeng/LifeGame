#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
import time

# 用户表，存储用户名与密码
class Room(models.Model):
    roomId = models.CharField(primary_key=True, max_length=255)
    user1 = models.CharField(max_length=255, default='')
    user2 = models.CharField(max_length=255, default='')
    info = models.TextField(default='')
    state = models.IntegerField(default=0)  # 0等待，1完成
    roomTime = models.DateTimeField(auto_now=True)  # 数据是否过期超时，暂不处理
    turnCount = models.IntegerField(default=0)  # 回合数(user2先手)，暂且认为每次操作是一个回合(真实回合可以除以二)
    
    def __unicode__(self):
        return self.id
        
    @staticmethod
    def getNewRoom():  # 17位数字字符串
        return str(time.time()).replace(".", "")
    
