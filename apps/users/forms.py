# -*- coding: utf-8 -*-
# @ IDE     : PyCharm
# @ File    : forms.py
# @ Author  : Rambo
# @ Time    : 2021-05-11 09:59


from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)


class DynamicLoginForm(forms.Form):
    # myfield = AnyOtherField()
    captcha = CaptchaField()