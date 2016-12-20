#!/usr/bin/python
# -*- coding: utf-8 -*-

'''视图'''

# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
 
from LifeGame.action.GameA import *
from LifeGame.action.FriendA import *
from LifeGame.action.ManagerA import *

def homePage(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/LifeGame/web/index.html'))

