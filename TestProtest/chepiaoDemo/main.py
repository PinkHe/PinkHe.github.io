import requests
import re
import base64
from PIL import Image
# from os import BytesIO

response = requests.get("https://kyfw.12306.cn/otn/resources/login.html")
erweima_image_base64_code = re.findall(r'<img id="J-qrImg" src="data:image/jpg;base64,(.*?)">', response.text)
print(erweima_image_base64_code)
code = base64.b64decode(erweima_image_base64_code[0])
with open("1.jpg",wb) as file:
    file.write(code)


print(re.text)
