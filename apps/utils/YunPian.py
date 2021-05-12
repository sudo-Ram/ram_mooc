# -*- coding: utf-8 -*-
# @ IDE     : PyCharm
# @ File    : YunPian.py
# @ Author  : Rambo
# @ Time    : 2021-05-12 16:02

import requests


def send_single_sms(apikey, code, mobile):
    # 发送单条短信
    url = "https://sms.yunpian.com/v2/sms/single_send.json"
    text = "云片网签名模板"
    # "【xxx】您的验证码是{}。非本人操作，请忽略本条短信。".format(code)

    response = requests.post(url, data={
        "apikey": apikey,
        "mobile": mobile,
        "text": text
    })
    return response


if __name__ == "__main__":
    response = send_single_sms("9a014f756490f24d15818aeea5dc1788", " ")
    import json
    res_json = json.loads(response.text)
    code = res_json["code"]
    msg = res_json["msg"]
    if code == 0:
        print("发送成功")
    else:
        print("发送失败:{}".format(msg))
    print(response.text)
