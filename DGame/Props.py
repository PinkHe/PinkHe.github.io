import DGUtils
import json
import uuid
import hashlib

excel_path = "./setfile/Props.xls"
temp_list = DGUtils.read_excel(excel_path)
with open("./setfile/set.json", "r", encoding="UTF-8") as DGsetJson:
    DGset = json.load(DGsetJson)
connect = DGUtils.connect_mysql(DGset)
cursor = connect.cursor()

resource = []
for i in temp_list[:]:
    dg_uuid = str(uuid.uuid4())
    i.insert(0, dg_uuid)
    temp = ""
    for j in i[1:]:
        temp = temp + j
    i.append(hashlib.sha1(temp.encode('UTF-8')).hexdigest())
    temp = tuple(i)
    resource.append(temp)

select_all_sign_sql = "SELECT Props_sign from dgprops "
cursor.execute(select_all_sign_sql)
all_sign_list = cursor.fetchall()

for i in all_sign_list:
    print(i) 
# print( all_sign_list)
# insert_sql = "insert into DGProps(Props_id,Props_name,Props_simpleChinese,Props_traditionalChinese,Props_kr,\
#     Props_en,Props_fr,Props_ge,Props_ru,Props_sp,Props_pt,Props_tr,Props_pl,Props_it,Props_sign) \
#     values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# cursor.executemany(insert_sql,resource)
# connect.commit()
    



   

# print(temp_list)


# ('Item_NameText1953044', '末世古龙', '末世古龙', '末世古龙', 'Ancient Eschaton Dragon', "Ancien Dragon d'Eschaton", 'Uralter Endzeitdrache', \
#     'Древний дракон конца света', 'Dragón escatón antiguo', '末世古龙', 'Kadim Kıyamet Ejderhası', '末世古龙', 'Antico Drago Eschaton')








