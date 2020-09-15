import DGUtils
import json
import uuid
import hashlib


# 读取道具文件
Props_excel_path = "./setfile/Props.xls"
props_list = DGUtils.read_excel(Props_excel_path)

# 读取道具文件
bannerTranslate_excel_path = "./setfile/bannerTranslate.xls"
bannerTranslate_list = DGUtils.read_excel(bannerTranslate_excel_path)

# 读取待验证的源文件
TranslateOrigin_excel_path = "./setfile/TranslateOrigin.xls"
TranslateOrigin_list = DGUtils.read_excel(TranslateOrigin_excel_path)


#读取数据库配置文件
with open("./setfile/set.json", "r", encoding="UTF-8") as DGsetJson:
    DGset = json.load(DGsetJson)
connect = DGUtils.connect_mysql(DGset)

# 调用函数，向道具表插入数据
insert_props_sql = "insert into DGProps(dgPropsId,dgPropsName,dgPropsSimpleChinese,dgPropsTraditionalChinese,dgPropsKr,\
        dgPropsEn,dgPropsFr,dgPropsGe,dgPropsRu,dgPropsSp,dgPropsPt,dgPropsTr,dgPropsPl,dgPropsIt,dgPropsSignCode) \
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# DGUtils.insert_fun(props_list, connect, insert_props_sql)


# 调用函数，向翻译表插入数据
insert_Translate_sql = "insert into dgtranslate(dgTranslateId, dgTranslateNum, dgTranslateUsePlace, dgTranslateCategory, dgTranslateUseTime, dgTranslateStartTime,\
        dgTranslateSimpleChinese, dgTranslateTraditionalChinese, dgTranslateKr, dgTranslateEn, dgTranslateFr, dgTranslateGe, dgTranslateRu,\
        dgTranslateSp, dgTranslatePt, dgTranslateTr, dgTranslatePl, dgTranslateIt, dgTranslateInfo, dgTranslateSignCode)\
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

DGUtils.insert_Translate_fun(bannerTranslate_list[:], connect, insert_Translate_sql, 8)


result_list = DGUtils.dg_hash_key(TranslateOrigin_list, 8)

select_all_dgtranslate_sign_sql = "SELECT * from dgtranslate "
select_all_dgProps_sign_sql = "SELECT * from dgProps "

db_dgtranslate_list = DGUtils.select_fun(connect, select_all_dgProps_sign_sql)
db_props_list = DGUtils.select_fun(connect, select_all_dgProps_sign_sql)

result_temp_list = []
for i in result_list[1:]:
    for j in db_dgtranslate_list:
        print(i[-1])
        print(j[-1])
        if i[-1] == j[-1]:
            
            result_temp_list.append(j)

for i in result_temp_list:
    print(i)
    
