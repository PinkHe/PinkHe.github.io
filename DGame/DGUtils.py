import pymysql
import uuid
import json
import xlrd
import unicodedata
import hashlib


import setfile

def select_fun(connect, sql):
    cursor = connect.cursor()
    cursor.execute(sql)
    result_list = cursor.fetchall()
    return result_list



# 向数据库去重插入数据
def insert_Translate_fun(temp_list,connect, insert_sql, num):
    cursor = connect.cursor()
    resource = []
    temp_list_hash = []
    for i in temp_list[:]:
        dg_uuid = str(uuid.uuid4())
        i.insert(0, dg_uuid)
        temp = ""
        temp_hash = ''
        for j in i[8:-1]:
            temp_hash += j[:num]
            temp_hash += j[-num:]
        temp_list_hash.append(temp_hash)
        temp_hash = hashlib.sha1(temp_hash.encode()).hexdigest()
        i.append(temp_hash)
        temp = tuple(i)#tuple()将列表转换成元组   扩展list()将元组转换成列表
        resource.append(temp)

    select_all_sign_sql = "SELECT dgTranslateSignCode from dgtranslate "
    cursor.execute(select_all_sign_sql)
    all_sign_list = cursor.fetchall()

    #提取出数据库中所有记录的hash值，避免重复插入数据
    sign_set = set()
    for i in all_sign_list:
        sign_set.add(i[0])


    #这里使用切片的原因：推测如果遍历的列表和删除数据的列表时同一个的话  在删除数据后数据的位置会发生变化（前移）   从而使得遍历数据发生跳过

    temp_resource = resource[:]
    for i in resource:
        if i[-1] in sign_set:
            temp_resource.remove(i)
    cursor.executemany(insert_sql,temp_resource)
    connect.commit()
    



#生成翻译特征码

def dg_hash_key(test_map, num):
     result_map = []
     for i in test_map[:]:
          temp_hash = ''
          for j in i[2:]:
               temp_hash += j[:num]
               temp_hash += j[-num:]
          temp_hash = unicodedata.normalize('NFKC', temp_hash)
          temp_hash = hashlib.sha1(temp_hash.encode()).hexdigest()
          i = list(i)
          i.append(temp_hash)
          result_map.append(i)
          
     return result_map


# 向数据库去重插入数据

def insert_fun(temp_list,connect, insert_sql):
    cursor = connect.cursor()
    resource = []
    for i in temp_list[:]:
        i[3],i[9],i[11] = i[4],i[4],i[4]
        dg_uuid = str(uuid.uuid4())
        i.insert(0, dg_uuid)
        temp = ""
        for j in i[1:]:
            temp = temp + j
        i.append(hashlib.sha1(temp.encode('UTF-8')).hexdigest())
        temp = tuple(i)#tuple()将列表转换成元组   扩展list()将元组转换成列表
        resource.append(temp)

    select_all_sign_sql = "SELECT dgPropsSignCode from dgProps "
    cursor.execute(select_all_sign_sql)
    all_sign_list = cursor.fetchall()

    #提取出数据库中所有记录的hash值，避免重复插入数据
    sign_set = set()
    for i in all_sign_list:
        sign_set.add(i[0])


    #这里使用切片的原因：推测如果遍历的列表和删除数据的列表时同一个的话  在删除数据后数据的位置会发生变化（前移）   从而使得遍历数据发生跳过

    temp_resource = resource[:]
    for i in resource:
        if i[-1] in sign_set:
            temp_resource.remove(i)
    print(temp_resource)
    
    cursor.executemany(insert_sql,temp_resource)
    connect.commit()
    



# 读取excel文件，
def read_excel(path):
   result_list = []
   with xlrd.open_workbook(path, encoding_override="UTF-8") as excel:
      table = excel.sheets()[0]
      nrows = table.nrows
      ncols = table.ncols
      i, j = 0, 0
      for i in range(0, nrows):
        temp_list = []
        for j in range(0, ncols):
            temp01 = table.row_values(i)[j] #得到数字列数据
            temp01 = str(temp01)
            cell = unicodedata.normalize('NFKC', temp01)#字符转换
            temp_list.append(cell)
        result_list.append(temp_list)
   return result_list

# with open("./setfile/set.json", "r", encoding="UTF-8") as DGsetJson:
#     DGset = json.load(DGsetJson)


# 创建数据库连接
def connect_mysql(set):
    #创建connect对象
    connect=pymysql.connect(set["host"], set["username"], set["password"], set["db_name"])
    
    return connect


# 关闭数据库连接
def close_mysql(connect):
    cursor = connect.cursor()
    cursor.close()
    connect.close()

    