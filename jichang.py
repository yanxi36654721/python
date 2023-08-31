import requests
import json


requests.packages.urllib3.disable_warnings()
base_url = 'https://linkhub.one'

addons = ""
def checkin():
    email = "1276013577@qq.com"
    password = "shitou123"

    email = email.split('@')
    email = email[0] + '%40' + email[1]

    session = requests.session()

    session.get(base_url, verify=False)

    login_url = base_url + '/auth/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    post_data = 'email=' + email + '&passwd=' + password + '&code='
    post_data = post_data.encode()
    response = session.post(login_url, post_data, headers=headers, verify=False)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Referer': base_url + '/user'
    }

    response = session.post(base_url + '/user/checkin', headers=headers, verify=False)
    print(response.text)
    decoded = response.text.encode('utf-8').decode('unicode_escape')

    # 通知模块
    url = "http://www.pushplus.plus/send"
    headers = {
        "Content-Type": "application/json;charset=utf-8"
    }

    # 构造POST请求的数据
    data = {
        "token": "8f5c754e7383481896aa0814d56495e4",  # 替换为您的key
        "title": "机场签到",  # 替换为您想要设置的消息标题
        "content": ""  # 替换为您想要发送的消息内容
    }
    data["content"] = decoded  # 将响应文本赋给变量
    # 发送POST请求
    response = requests.post(url, headers=headers, json=data)

while True:
    try:
        checkin()
    except Exception:
        continue
    break
