from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        user_name = request.POST.get("username", "")
        password = request.POST.get("password", "")

        # 验证规则过于冗余繁琐
        # if not user_name:
        #     return render(request, "login.html", {"msg": "请输入用户名"})
        # if not password:
        #     return render(request, "login.html", {"msg": "请输入密码"})
        # if len(password) < 3:
        #     return render(request, "login.html", {"msg": "密码格式不正确"})

        # 使用表单验证可简化

        # 用于通过用户和密码查询用户是否存在
        user = authenticate(username=user_name, password=password)

        # 1.通过用户名查询到用户
        # 2.需要先加密再通过加密之后的密码查询
        # from apps.users.models import UserProfile
        # user = UserProfile.objects.get(username=user_name, password=password)

        if user is not None:
            # 查询到用户
            login(request, user)
            # 登陆成功之后该如何返回页面
            return HttpResponseRedirect(reverse("index"))
        else:
            # 未查询到用户
            return render(request, "login.html", {"msg": "用户名或密码错误"})

