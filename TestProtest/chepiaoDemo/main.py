import requests
import re
import base64
from PIL import Image
# from os import BytesIO
session = requests.Session()
# response = requests.get("https://kyfw.12306.cn/otn/resources/login.html")
# erweima_image_base64_code = re.findall(r'<img id="J-qrImg" src="data:image/jpg;base64,(.*?)">', response.text)
# print(erweima_image_base64_code)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Referer": "https://kyfw.12306.cn/",
}
check_image_param = {
    "login_site":"E",
    "module":"login",
    "rand":"sjrand",
    "1609907365072":"",
    "callback":"jQuery191015651958309848935_1609907331059",
    "_":"1609907331060",
}
session.get("https://kyfw.12306.cn/otn/resources/login.html")
check_image_url = "https://kyfw.12306.cn/passport/captcha/captcha-image64"
response = session.get(url=check_image_url,params=check_image_param,headers=headers)
check_image_code_encodeB64 = re.findall(r'"image":"(.*?)"',response.text)
decode_check_image_code = base64.b64decode(check_image_code_encodeB64[0])
with open("1.jpg","wb") as file:
    file.write(decode_check_image_code)

point = {
    "1": "40,40",
    "2": "120,40",
    "3": "180,40",
    "4": "250,40",
    "5": "40,100",
    "6": "120,100",
    "7": "180,100",
    "8": "250,100",
}
check_list_str = input("请输入验证码坐标：")

check_list = check_list_str.split(",")
answer = ''
for i in check_list:
    answer += point.get(i)
    if i != check_list[-1]:
        answer += ','

callback_check_image_url="https://kyfw.12306.cn/passport/captcha/captcha-check"
check_image_param = {
    "callback":"jQuery191036962453111752835_1609908697139",
    "answer":answer,
    "rand":"sjrand",
    "login_site":"E",
    "_":"1609908697142",
}

callback_check_image_response = session.get(url=callback_check_image_url, params=check_image_param, headers=headers)
# print(callback_check_image_response.text)
user_info = {
    "username":"18781224173",
    "password":"08394417959hhj",
    "appid":"otn",
}
login_url = "https://kyfw.12306.cn/passport/web/login"
login_response = session.post(url=login_url, params=user_info, headers=headers)
login_response = session.get('https://kyfw.12306.cn/otn/view/index.html')
print(login_response.headers)
print(login_response.text)
