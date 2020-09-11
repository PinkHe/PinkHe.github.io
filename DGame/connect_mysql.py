import pymysql
import uuid
host="localhost"
username="root"
password="123456"
db_name="pythontest"
#创建connect对象
connect=pymysql.connect(host,username,password,db_name)
#获取游标对象
cursor=connect.cursor()

select_all_sql = "select * from gmtable"
#批量插入数据
'''
resouces = [
    ("2","2","2","2","2","2"),
    ("3","3","3","3","3","3"),
    ("4","4","4","4","4","4"),
]

insert_sql = "insert into gmtable(Gmid,GmName,GmInfo,Gmbody,GmExample,GmExampleInfo) \
    values(%s, %s, %s, %s, %s, %s)"
cursor.executemany(insert_sql,resouces)
connect.commit()
'''
print("请输入Gm名称")

print("请输入Gm描述")

print("请输入Gm命令")

print("请输入Gm举例")

print("请输入举例描述")

cursor.execute(select_all_sql)
#result=cursor.fetchone()

result=cursor.fetchall()
print(result)
cursor.close()
connect.close()