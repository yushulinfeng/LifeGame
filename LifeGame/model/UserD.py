#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
import time

# Token表
class Token(models.Model):
    tokenId = models.CharField(primary_key=True, max_length=255)
    tokenTime = models.DateTimeField(auto_now=True)  # 数据是否过期超时，暂不处理
    roomId = models.CharField(max_length=255, default='')
    tokenText = models.TextField(default='')
    
    def __unicode__(self):
        return self.tokenId
    
    @staticmethod
    def getNewToken():  # 17位数字字符串
        return str(time.time()).replace(".", "")
