import requests

re = requests.get("https://kyfw.12306.cn/otn/resources/login.html")


print(re.text)