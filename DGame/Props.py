import DGUtils
import json
import uuid
import hashlib

excel_path = "./setfile/Props.xls"
temp_list = DGUtils.read_excel(excel_path)
with open("./setfile/set.json", "r", encoding="UTF-8") as DGsetJson:
    DGset = json.load(DGsetJson)
connect = DGUtils.connect_mysql(DGset)

# 调用函数，向数据库插入数据
DGUtils.insert_fun(temp_list, connect)






