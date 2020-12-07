import re
import requests
import base64



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
    url = urls_header + url_body
    respose=requests.get(url, headers = header)
    urls_01 = re.findall(r'<a href="(.*?)" alt=".*?" title=".*?"></a>',respose.text)
    # filename = 1
    for i in urls_01:
        filename = i.split('/')[-1]
        
        url = 'https://'+i[2:]
        respose=requests.get(url,headers = header)
        with open('./result_file/'+filename, 'wb') as file:
            file.write(respose.content)
            file.close()

# video=requests.get(mp4_url)

# with open('E:\PythonProject\PinkHe.github.io\TestProtest\reptilesDemo\result_filea\a.mp4','wb') as f:
#     f.write(video.content)