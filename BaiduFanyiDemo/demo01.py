#http://api.fanyi.baidu.com/api/trans/vip/translate   api接口

import requests
import hashlib

import time
import ast
import FanyiUtil
import json


# language = {
#   'auto':'自动','zh':'中文','en':'英语','yue':'粤语','wyw':'文言文','jp':'日语','kor':'韩语','fra':'法语','spa':'西班牙语',
#   'th':'泰语','ara':'阿拉伯语','ru':'俄语','pt':'葡萄牙语','de':'德语','it':'意大利语','el':'希腊语','nl':'荷兰语','pl':'波兰语',
#   'bul':'保加利亚语','est':'爱沙尼亚语','dan':'丹麦语','fin':'芬兰语','cs':'捷克语','rom':'罗马尼亚语','slo':'斯洛文尼亚语','swe':'瑞典语','hu':'匈牙利语',
#   'cht':'繁体中文','vie':'越南语'
# }
with open('languageJson.json', 'r', encoding='UTF-8') as languageJson:
  language = json.load(languageJson)



def fanyi_request(baidu_q,baidu_from,baidu_to,baidu_appid,baidu_salt,baidu_key):
  baidu_sign = baidu_appid + baidu_q + baidu_salt + baidu_key
  m = hashlib.md5(baidu_sign.encode(encoding='UTF-8'))

  url = "http://api.fanyi.baidu.com/api/trans/vip/translate?q="+baidu_q+"&from="+baidu_from+"&to="+baidu_to+"&appid="+baidu_appid+"&salt="+baidu_salt+"&sign="+m.hexdigest()
  payload = {}
  headers = {
  'Cookie': 'BAIDUID=F78C4D8087215921BC7B570A31E98FF3:FG=1'
  } 
  response = requests.request("GET", url, headers=headers, data = payload)
  print(response.text.encode('utf8'))
  return response.text.encode('utf8')



baidu_q = "哈哈哈"
baidu_from = "auto"
baidu_to = "zh"
baidu_appid = "20200907000560666"
baidu_salt = FanyiUtil.baidu_random(10)
baidu_key = "wMFrWoYig_cQsShGChJK"
baidu_sign = baidu_appid + baidu_q + baidu_salt + baidu_key
m = hashlib.md5(baidu_sign.encode(encoding='UTF-8'))
print(baidu_sign)

print(m.hexdigest())

baidu_q_list = FanyiUtil.file_read('file.text', 'UTF-8')

result_list = []

for i in baidu_q_list:
  baidu_salt = FanyiUtil.baidu_random(10)
  temp_str = fanyi_request(i,baidu_from,baidu_to,baidu_appid,baidu_salt,baidu_key)
  temp_str = str(temp_str,'UTF-8')
  result_list.append(temp_str)
  time.sleep(1)

print(result_list)

result_dict_list = []

for i in result_list:
  temp_dict = ast.literal_eval(i)
  result_dict_list.append(temp_dict)

for i in result_dict_list:
  if i["from"] not in language:
    print("识别失败")
  else:
    print(language[i["from"]])
  
  





  











