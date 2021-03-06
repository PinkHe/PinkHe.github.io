import random
import requests
import hashlib
import xlrd



def file_read(name, code):
   result_list = []
   with open(name, 'r',encoding=code) as file:
      temp_list = file.readlines()
      for i in temp_list:
         result_list.append(i.rstrip('\n')) 
      return result_list


def baidu_random(n):
   call_str = ""
   for i in range(0, n):
      call_str += str(random.randint(0,9))
   return call_str

def fanyi_request(baidu_q,baidu_from,baidu_to,baidu_appid,baidu_salt,baidu_key):
  baidu_sign = baidu_appid + baidu_q + baidu_salt + baidu_key
  m = hashlib.md5(baidu_sign.encode(encoding='UTF-8'))

  url = "http://api.fanyi.baidu.com/api/trans/vip/translate?q="+baidu_q+"&from="+baidu_from+"&to="+baidu_to+"&appid="+baidu_appid+"&salt="+baidu_salt+"&sign="+m.hexdigest()
  payload = {}
  headers = {
  'Cookie': 'BAIDUID=F78C4D8087215921BC7B570A31E98FF3:FG=1'
  } 
#   response = requests.request("GET", url, headers=headers, data = payload)
  response = requests.get(url)
#   response =  requests.post(url)
  print("数据校验中...")
  return response.text.encode('utf8')

def read_excel(path):
   result_list = []
   with xlrd.open_workbook(path, encoding_override="UTF-8") as excel:
      table = excel.sheets()[0]
      nrows = table.nrows
      ncols = table.ncols
      i, j = 0, 0
      for i in range(0, nrows):
         for j in range(0, ncols):
            cell = table.row_values(i)[j] #得到数字列数据
            result_list.append(cell)
   return result_list