import pymysql
host="localhost"
username="root"
password="123456"
db_name="pythontest"
#创建connect对象
connect=pymysql.connect(host,username,password,db_name)
#获取游标对象
cursor=connect.cursor()

select_sql = "select * from student"


cursor.execute(select_sql)
#result=cursor.fetchone()

result=cursor.fetchall()
print(result)
cursor.close()
connect.close()