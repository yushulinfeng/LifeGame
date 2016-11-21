#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

from django.core.wsgi import get_wsgi_application

# 配置到wsgi服务器需要添加这一句
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LifeGame_Server.settings")

application = get_wsgi_application()

