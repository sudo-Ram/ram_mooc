# -*- coding: utf-8 -*-
# @ IDE     : PyCharm
# @ File    : adminx.py
# @ Author  : Rambo
# @ Time    : 2021-05-08 11:20


import xadmin
from xadmin import views


class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "慕学在线网"
    # menu_style = "accordion"


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
