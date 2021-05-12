from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.users.forms import LoginForm, DynamicLoginForm


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        # 重定向跳转，转首页配置"index"，转登录界面配置"login"
        return HttpResponseRedirect(reverse("login"))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))

        login_form = DynamicLoginForm()
        return render(request, "login.html", {
            "login_form": login_form
        })

    def post(self, request, *args, **kwargs):
        # 使用表单验证可简化
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            # 用于通过用户和密码查询用户是否存在
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
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
                return render(request, "login.html", {"msg": "用户名或密码错误", "login_form": login_form})
        else:
            return render(request, "login.html", {"login_form": login_form})

        # 验证规则过于冗余繁琐
        # if not user_name:
        #     return render(request, "login.html", {"msg": "请输入用户名"})
        # if not password:
        #     return render(request, "login.html", {"msg": "请输入密码"})
        # if len(password) < 3:
        #     return render(request, "login.html", {"msg": "密码格式不正确"})
