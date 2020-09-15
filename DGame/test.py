import hashlib


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

s = 'Keep operewards!Keep operewards!Continuelusives!Öffne daewinnen!Продолжа награды¡Sigue alusivos!Keep operewards!Özel etkevam et!Keep operewards!Continua eventi!'
temp = hashlib.sha1(s.encode("UTF-8")).hexdigest()
print(temp)
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