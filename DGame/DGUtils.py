import pymysql
import uuid
import json
import xlrd
import unicodedata
import hashlib


import setfile



# 向数据库去重插入数据

def insert_fun(temp_list,connect):
    cursor = connect.cursor()
    resource = []
    for i in temp_list[:]:
        dg_uuid = str(uuid.uuid4())
        i.insert(0, dg_uuid)
        temp = ""
        for j in i[1:]:
            temp = temp + j
        i.append(hashlib.sha1(temp.encode('UTF-8')).hexdigest())
        temp = tuple(i)#tuple()将列表转换成元组   扩展list()将元组转换成列表
        resource.append(temp)

    select_all_sign_sql = "SELECT Props_sign from dgprops "
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
    insert_sql = "insert into DGProps(Props_id,Props_name,Props_simpleChinese,Props_traditionalChinese,Props_kr,\
        Props_en,Props_fr,Props_ge,Props_ru,Props_sp,Props_pt,Props_tr,Props_pl,Props_it,Props_sign) \
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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

    