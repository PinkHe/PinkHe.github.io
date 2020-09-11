#http://api.fanyi.baidu.com/api/trans/vip/translate   api接口

import requests
import hashlib
import time
import ast
import FanyiUtil
import json
import unicodedata



with open('languageJson.json', 'r', encoding='UTF-8') as languageJson:
  language = json.load(languageJson)

with open('userInfo.json', 'r', encoding='UTF-8') as userInfoJson:
  userInfo = json.load(userInfoJson)

# baidu_q_list = FanyiUtil.file_read('file.text', 'UTF-8')
  baidu_q_list = FanyiUtil.read_excel("test.xls")

result_list = []
# 发送请求
for i in baidu_q_list:
  i = unicodedata.normalize('NFKC', i)#字符转换
  baidu_salt = FanyiUtil.baidu_random(10)
  temp_str = FanyiUtil.fanyi_request(i,userInfo['baidu_from'],userInfo['baidu_to'],userInfo['baidu_appid'],baidu_salt,userInfo['baidu_key'])
  temp_str = str(temp_str,'UTF-8')
  result_list.append(temp_str)
  time.sleep(1)

result_dict_list = []
# 将返回的字节串转换成字典
for i in result_list:
  temp_dict = ast.literal_eval(i)
  result_dict_list.append(temp_dict)

print("识别结果为：")
for i in result_dict_list:
  if i["from"] not in language:
    print("识别失败",end='___')
  else:
    print(language[i["from"]],end='___')
  
  print(i["trans_result"])
  
  
