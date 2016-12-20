#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views import static
from LifeGame import views
from LifeGame_Server import settings

# 部署项目到WSGI时，设置此值为True，然后设置URL为webhost即可
# 从而实现维持项目一致性不变，并且最少修改
# \\在Linux中存在问题，应该使用/确保通用
wsgi = True

webhost = 'LifeGame/'
if wsgi:
    webhost = ''

urlpatterns = [
    # url(r'^$', views.homePage),  # 直接主页
    url(r'^' + webhost + '$', views.homePage, name='LifeGame'),  # 主页(限制^$，禁止get)
    # 静态页面目录
    url(r'^' + webhost + 'web/(.*)$', static.serve, \
         { 'document_root': settings.STATIC_ROOT }),
    # 管理员
    url(r'^' + webhost + 'manager$', views.manage),
    url(r'^' + webhost + 'managerLogin$', views.managerLogin),
    url(r'^' + webhost + 'managerHtml$', views.managerHtml),
    # 接口
    url(r'^' + webhost + 'test$', views.test),  # 
    url(r'^' + webhost + 'GameSetting$', views.gameSetting),  # 
    url(r'^' + webhost + 'GameStart$', views.gameStart),  # 
    url(r'^' + webhost + 'GameRefresh$', views.gameRefresh),  # 
    # 新的
    url(r'^' + webhost + 'TokenGet$', views.tokenGet),  # 
    url(r'^' + webhost + 'MatchFriend$', views.matchFriend),  # 
    url(r'^' + webhost + 'MatchState$', views.matchState),  # 
    url(r'^' + webhost + 'GameState$', views.gameState),  # 
    url(r'^' + webhost + 'GameUpload$', views.gameUpload),  # 
]

