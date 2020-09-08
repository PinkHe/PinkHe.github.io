import random



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