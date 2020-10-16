import hashlib
import re
import datetime
import sys

sys.path.append("../..")
sys.path.append("..")
# print(sys.path)

import DGUtils





def start_server_day(day_list, sign_start_time, boolean):
     if boolean:
          sign_start_time = datetime.datetime.strptime(sign_start_time, '%Y-%m-%d %H:%M:%S')
          left_start_time = sign_start_time - datetime.timedelta(days=int(day_list[0])-1)
          right_start_time = sign_start_time - datetime.timedelta(days=int(day_list[1])-1)
          # 通过timetuple函数将日期转化成结构体数据类型，然后自己拼接日期格式
          time = datetime.datetime.timetuple(left_start_time)
          left_start_time = str(time.tm_year) + ',' + str(time.tm_mon) + ',' + str(time.tm_mday) + ',' + "23,59,59" 
          time = datetime.datetime.timetuple(right_start_time)
          right_start_time = str(time.tm_year) + ',' + str(time.tm_mon) + ',' + str(time.tm_mday) + ',' + "0,0,0"
     else:
          sign_start_time = datetime.datetime.strptime(sign_start_time, '%Y-%m-%d %H:%M:%S')
          left_start_time = sign_start_time - datetime.timedelta(days=int(day_list[0])-1)
          # right_start_time = sign_start_time - datetime.timedelta(days=int(day_list[1])-1)
          # 通过timetuple函数将日期转化成结构体数据类型，然后自己拼接日期格式
          time = datetime.datetime.timetuple(left_start_time)
          left_start_time = str(time.tm_year) + ',' + str(time.tm_mon) + ',' + str(time.tm_mday) + ',' + "23,59,59" 
          # time = datetime.datetime.timetuple(right_start_time)
          # right_start_time = str(time.tm_year) + ',' + str(time.tm_mon) + ',' + str(time.tm_mday) + ',' + "0,0,0"
          right_start_time = "2019,1,1,0,0,0"
     return right_start_time + "," + left_start_time


# 计算文档中的开服天数对应日期
def fun_start_day():
     print("请输入活动开始生效的时间 eg:2020-10-09")
     start_time = input()
     start_time = start_time + " 00:00:00"

     path = "./../Demo01File/eg.xls"
     list_01 = DGUtils.read_excel(path)

     day_list = [x for x in list_01 if "开服" in str(x)]
     # for i in list_01:
     #      if "开服" in str(i):
     #           print(i)

     day_list_int = []

     for i in day_list:
          # 正则提取出开服天数段数据
          day = re.findall(r'开服[0-9]+天', str(i))
          if len(day) == 0:
               day = re.findall(r'开服[0-9]+-[0-9]+天', str(i))
         
          # 正则提取出开服天数段数据（纯数字）
          int_day = re.findall("\d+",str(day))
          day_list_int.append(int_day)


     result_day_text = ""

     for day_list in day_list_int:
          
          if len(day_list) > 0: # 过滤掉部分干扰数据
               if len(day_list) < 2:
                    result_day_text += start_server_day(day_list, start_time, False) + "\n"    
               else:
                    result_day_text += start_server_day(day_list, start_time, True) + "\n"
               

     with open("./../Demo01File/result.txt", "w", encoding="UTF-8") as file:
          file.write(result_day_text)
          print("写入结果到result.txt文件完成")
          print()

# 整理源日期格式
def fun_zhengli():

     with open("./../Demo01File/origin.txt", "r", encoding="UTF-8") as file:
          list01 = file.readlines()

     temp_str = "" 
     for i in list01:
          temp_str += str(i)

     temp_str = temp_str.replace("|","\n")

     with open("./../Demo01File/origin_result.txt", "w", encoding="UTF-8") as file:
          file.write(temp_str)
     with open("./../Demo01File/origin_result.txt", "r", encoding="UTF-8") as file:
          list01 = file.readlines()


     for i in range(0,len(list01)):
          list01[i] = list01[i].split(",")
          list01[i][0] = list01[i][0].replace("(","")
          del list01[i][-1]

     result_str_list = []

     for i in list01:
          str_temp = ""
          for j in range(0,len(i)):
               if j == len(i)-1:
                    str_temp += i[j]
               else:
                    str_temp += i[j]
                    str_temp += ","
          result_str_list.append(str_temp)

     with open("./../Demo01File/origin_result.txt", "w", encoding="UTF-8") as file:
          for i in result_str_list:
               file.write(str(i))
               file.write("\n")

          
          print("整理结果已写入 origin_result.txt 文档")
          print()

while True:
     print("说明：配置文档请写入eg.xls文件")
     print("说明：计算结果讲写入result.txt文件")
     print("说明：待整理文件请写入origin.xls文件")
     print()
     print("请选择功能：")
     print("输入  1  ：计算文档 eg.xls 中的开服天数所对应的日期") 
     print("输入  2  ：整理文档 origin.txt 中的数据格式")
     print("输入  3  ：退出")

     input_num = input()

     if "1" == input_num:
          fun_start_day()
     elif "2" == input_num:
          fun_zhengli()
     elif "3" == input_num:
          break
     else:
          print("输入的数据有误")











































# a = ["1","2","3"]

# b = ["2","3"]

# print(a-b)

# def dg_hash_key(test_map, num):
#      result_map = []
#      for i in test_map[:]:
#           temp_hash = ''
#           for j in i[2:]:
#                i = unicodedata.normalize('NFKC', j)
#                temp_hash += j[:num]
#                temp_hash += j[-num:]

#           print("凭借未" + temp_hash)
#           temp_hash = hashlib.sha1(temp_hash.encode()).hexdigest()
#           print("凭借未哈哈哈" + temp_hash)
#           i = list(i)
#           i.append(temp_hash)
#           result_map.append(i)
          
#      return result_map



'''
test_map = [
     ("19","29","h5ahhah4kk","j5kkjkjsx4sjjak","j5shjah4sas"),
     ("18","28","h5ahhah3kk","j5kkjkjsx3sjjak","j5shjah 3sas"),
     ("11","21","h1ahhah XXX kk","j1kkjkjsx XXX sjjak","j1shjah XXX sas"),
     ("12","22","h2ahhah XXX kk","j2kkjkjsx XXX sjjak","j2shjah XXX sas"),
     ("13","23","h3ahhah XXX kk","j3kkjkjsx XXX sjjak","j3shjah XXX sas"),
     ("14","24","h4ahhah XXX kk","j4kkjkjsx XXX sjjak","j4shjah XXX sas"),
     ("15","25","h5ahhah xxx kk","j5kkjkjsx XXX sjjak","j5shjah XXX sas"),
     ("16","26","h6ahhah6kk","j5kkjkjsx6sjjak","j5shjah6as"),
     ("17","27","h7ahhahkk","j7kkjkjsxsjjak","j75shjahsas")
]

input_map = [
     ("19","29","h5ahhah4kk","j5kkjkjsx4sjjak","j5shjah4sas"),
     ("18","28","h5ahhah3kk","j5kkjkjsx3sjjak","j5shjah 3sas"),
     ("11","21","h1ahhah aa kk","j1kkjkjsx bb sjjak","j1shjah cc sas"),
     ("12","22","h2ahhah dd kk","j2kkjkjsx hh sjjak","j2shjah nn sas"),
     ("13","23","h3ahhah XXX kk","j3kkjkjsx XXX sjjak","j3shjah XXX sas"),
     ("14","24","h4ahhah XXX kk","j4kkjkjsx XXX sjjak","j4shjah XXX sas"),
     ("15","25","h5ahhah xxx kk","j5kkjkjsx XXX sjjak","j5shjah XXX sas"),
     ("16","26","h6ahhah6kk","j5kkjkjsx6sjjak","j5shjah6as"),
     ("17","27","h7ahhahkk","j7kkjkjsxsjjak","j75shjahsas")
]


props_list = [
     ("1a","2a","aa","bb","cc"),
     ("1d","2d","dd","hh","nn"),
     ("1e","2e","ee","ii","mm"),
     ("1f","2f","ff","jj","kk")
]

def dg_hash_key(test_map, num):
     result_map = []
     for i in test_map[:]:
          temp_hash = ''
          for j in i[2:]:
               temp_hash += j[:num]
               temp_hash += j[-num:]
          temp_hash = hashlib.sha1(temp_hash.encode('UTF-8')).hexdigest()
          i = list(i)
          i.append(temp_hash)
          result_map.append(i)
     return result_map

result_map_01 = dg_hash_key(test_map, 2)

for i in result_map_01:
     print(i)

'''

# s = 'Keep operewards!Keep operewards!Continuelusives!Öffne daewinnen!Продолжа награды¡Sigue alusivos!Keep operewards!Özel etkevam et!Keep operewards!Continua eventi!'
# temp = hashlib.sha1(s.encode("UTF-8")).hexdigest()
# print(temp)
# resule_list = []
# for i in test_map:
#      if "XXX" in i[2]:
#           resule_list.append(i)
#      else :
#           print("插入数据成功")

# result_list = []
# for i in resule_list:
#      temp_list = []
#      for j in i:
#           if "XXX" in j:
#                j = j.replace('XXX', '哈哈哈')
#                temp_list.append(j)
#           else:
#                temp_list.append(j)
#      temp_list = tuple(temp_list)
#      result_list.append(temp_list)
     

# for i in resule_list:
#      print(i)

# for i in result_list:
#      print(i)






'''
s = ['(1,2)','(1,3)','(1,4)','(1,5)','(1,6)']

a = ['(1,2)','(1,3)','(1,4)']


for i in s:
     if i in a:
          s.remove(i)
print(s)
'''