import re
import requests
from PIL import Image
from io import BytesIO
import base64
import time
import os
import sys



header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Referer': 'https://www.vmgirls.com/',
}
respose=requests.get('https://www.vmgirls.com/',headers = header)
# print(respose.status_code)# 响应的状态码
# print(respose.content)  #返回字节信息
# print(respose.text)  #返回文本内容
# urls=re.findall(r'<a href="(.*?)" alt=".*?" title=".*?"></a>',respose.text)  #re.S 把文本信息转换成1行匹配
urls=set(re.findall(r'[1-9][0-9]*.html',respose.text))

urls_header = 'https://www.vmgirls.com/'
for url_body in urls:
    time.sleep(1)
    url = urls_header + url_body
    respose=requests.get(url, headers = header)
    urls_01 = re.findall(r'<a href="(.*?)" alt=".*?" title=".*?">.*</a>',respose.text)
    dirname = re.findall(r'<h1 class=".*?">(.*?)</h1>',respose.text)
    dir_path = './result_file/'+dirname[0]
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    # print(urls_01)
    # filename = 1
    for i in urls_01:
        filename = i.split('/')[-1]
        
        url = 'https://'+i[2:]
        print(url)
        respose=requests.get(url,headers = header)
        # print(respose.content)
        # decodebase64_source = base64.b64decode(respose.content)
        # print(os.path.isdir('./../result_file/'))
        temp_image = Image.open(BytesIO(respose.content))
        temp_image.save(dir_path+'/'+filename)
        # with open('./result_file/'+filename, 'wb') as file:
        #     file.write(respose.content)
        #     file.close()

# video=requests.get(mp4_url)

# with open('E:\PythonProject\PinkHe.github.io\TestProtest\reptilesDemo\result_filea\a.mp4','wb') as f:
#     f.write(video.content)