import pymysql
import uuid
import setfile
import json
import xlrd
import unicodedata


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

with open("./setfile/set.json", "r", encoding="UTF-8") as DGsetJson:
    DGset = json.load(DGsetJson)

def connect_mysql(set):
    #创建connect对象
    connect=pymysql.connect(set["host"], set["username"], set["password"], set["db_name"])
    
    return connect

def close_mysql(connect):
    cursor = connect.cursor()
    cursor.close()
    connect.close()

# connect = connect_mysql(DGset)
# cursor = connect.cursor()
# select_all_sql = "select * from DGProps"
# cursor.execute(select_all_sql)
# temp = result=cursor.fetchone()
# print(temp)
    #获取游标对象
    # cursor=connect.cursor()
    # select_all_sql = "select * from gmtable"
    # #批量插入数据
    # '''
    # resouces = [
    #     ("2","2","2","2","2","2"),
    #     ("3","3","3","3","3","3"),
    #     ("4","4","4","4","4","4"),
    # ]

    # insert_sql = "insert into gmtable(Gmid,GmName,GmInfo,Gmbody,GmExample,GmExampleInfo) \
    #     values(%s, %s, %s, %s, %s, %s)"
    # cursor.executemany(insert_sql,resouces)
    # connect.commit()
    # '''
    # print("请输入Gm名称")

    # print("请输入Gm描述")

    # print("请输入Gm命令")

    # print("请输入Gm举例")

    # print("请输入举例描述")

    # cursor.execute(select_all_sql)
    # #result=cursor.fetchone()

    # result=cursor.fetchall()
    # print(result)
    # cursor.close()
    # connect.close()
    