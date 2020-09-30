import DGUtils
import json
import uuid
import hashlib
import xlwt

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

# DGUtils.insert_Translate_fun(bannerTranslate_list[:], connect, insert_Translate_sql, 8)


result_list = DGUtils.dg_hash_key(TranslateOrigin_list, 8)

select_all_dgtranslate_sign_sql = "SELECT * from dgtranslate "
select_all_dgProps_sign_sql = "SELECT * from dgProps "

db_dgtranslate_list = DGUtils.select_fun(connect, select_all_dgtranslate_sign_sql)
db_props_list = DGUtils.select_fun(connect, select_all_dgProps_sign_sql)

#没有匹配记录的翻译
error_dgtranslate_list = []

#获取提交的翻译对应的库记录
result_temp_list = []
for i in result_list[1:]:
    for j in db_dgtranslate_list:
        if i[-1] == j[-1]:
            result_temp_list.append(j)

# true_dgtranslate_list = [x for x in result_temp_list if x in result_list[1:]] #两个列表中的相同元素
# error_dgtranslate_list = [y for y in (result_temp_list + result_list[1:]) if y not in true_dgtranslate_list] #两个列表中的不同元素
#包含XXXX的库中的特征码记录
xxxx_signcode_replace_list = []
#包含XXXX的库中的记录
xxxx_replace_list = []

for i in result_temp_list:
    if "XXXX" in i[9]:
        xxxx_signcode_replace_list.append(i[-1])
        xxxx_replace_list.append(i)

#待检查翻译的的包含XXXX的记录
xxxx_origin_replace_list = []

for i in result_list[1:]:
    for j in xxxx_signcode_replace_list:
        if j == i[-1]:
            xxxx_origin_replace_list.append(i)

#最匹配的道具信息记录
replace_props_list = []

result = ''
for i in xxxx_origin_replace_list:
    result_length = 0
    
    for j in db_props_list:
        if j[5] in i[2]:
            if len(j[5]) > result_length:
                result = j
                result_length = len(j[5])
    replace_props_list.append(result)

xxxx_replace_list_temp = []
for i in xxxx_replace_list:
    xxxx_replace_list_temp.append(list(i)) 

# 讲包含XXXX的翻译进行替换
for i in range(0, len(xxxx_replace_list_temp)):
    for j in range(0, len(xxxx_replace_list_temp[i])-10):
        if 'XXXX' in xxxx_replace_list_temp[i][j+8]:
            xxxx_replace_list_temp[i][j+8] = xxxx_replace_list_temp[i][j+8].replace('XXXX', replace_props_list[i][j+4])
    xxxx_replace_list_temp[i] = tuple(xxxx_replace_list_temp[i])


    
for i in xxxx_replace_list_temp:
    for j in range(0, len(result_temp_list)):
        if i[0] == result_temp_list[j][0]:
            result_temp_list[j] = i

# 将末尾的特征码替换成换行符，方便在写入文本文件时自动换行
# for i in range(0, len(result_temp_list)):
#     result_temp_list[i] = list(result_temp_list[i])
#     result_temp_list[i][-1] = "\n"
#     result_temp_list[i] = tuple(result_temp_list[i])



# with open("result.txt", 'w',encoding="UTF-8") as file:
#     for i in result_temp_list:
#         file.writelines(i)
    
workbook = xlwt.Workbook(encoding='utf-8')
booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)

header = ["Id","编号","用途","分类","使用时间","开始时间","简中","繁中","韩语","英语","法语","德语","俄语","西班牙语","葡萄牙语","土耳其语","波兰语","意大利语","说明"]
# 写列头
row = 0
for col in range(len(header)):
    booksheet.write(row, col, header[col])

 # 写内容
for lines in result_temp_list:
    row += 1
    for col in range(len(lines)):
        booksheet.write(row, col, lines[col])
if error_dgtranslate_list is not None:
    row += 1
    booksheet.write(row, 0, "未定义的条目如下：")
    for lines in error_dgtranslate_list:
        row += 1
        for col in range(len(lines)):
            booksheet.write(row, col, lines[col])

# 保存文件
workbook.save("result.xls")

        
    
print("执行完成，执行结果为result.xls")
    
# print(true_dgtranslate_list)