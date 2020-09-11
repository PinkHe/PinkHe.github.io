import xlrd
import unicodedata
import ast
import hashlib



# 单充任选寻宝令，开启寻宝之旅拿红色装备！	單充任選尋寶令，開啟尋寶之旅拿紅色裝備！	Free Self-choose Keys for Single Purchase; Start your adventure and get some Red Equipment!	Free Self-choose Keys for Single Purchase; Start your adventure and get some Red Equipment!	Clés de Sélection Gratuites pour un Achat Unique ; Commencez votre aventure et obtenez de l'Équipement Rouge !	Selbstgewählte Gratis-Schlüssel zum Einzelkauf; starte dein Abenteuer und erhalte einige Rote Ausrüstung!	Бесплатные ключи на выбор для одной покупки! Начните свое приключение и получите красное снаряжение!	Llaves de autoelección gratuitas para compra individual: ¡comienza tu aventura y consigue equipo rojo!	Free Self-choose Keys for Single Purchase; Start your adventure and get some Red Equipment!	Tek Satın Almaya Ücretsiz Kendin Seçmeli Anahtarlar: Macerana başla ve Kırmızı Ekipman kazan!	Free Self-choose Keys for Single Purchase; Start your adventure and get some Red Equipment!	Tasti di Scelta Automatica Gratuiti per Acquisto Singolo; Inizia la tua avventura e ottieni Equipaggiamento Rosso!





s = "Free Self-choose Keys for Single Purchase; Start your adventure and get some Red Equipment!	Free Self-choose Keys for Single Purchase; Start your adventure and get some Red Equipment!	Clés de Sélection Gratuites pour un Achat Unique ; Commencez votre aventure et obtenez de l'Équipement Rouge !	Selbstgewählte Gratis-Schlüssel zum Einzelkauf; starte dein Abenteuer und erhalte einige Rote Ausrüstung!	Бесплатные ключи на выбор для одной покупки! Начните свое приключение и получите красное снаряжение!	Llaves de autoelección gratuitas para compra individual: ¡comienza tu aventura y consigue equipo rojo!	Free Self-choose Keys for Single Purchase; Start your adventure and get some Red Equipment!	Tek Satın Almaya Ücretsiz Kendin Seçmeli Anahtarlar: Macerana başla ve Kırmızı Ekipman kazan!	Free Self-choose Keys for Single Purchase; Start your adventure and get some Red Equipment!	Tasti di Scelta Automatica Gratuiti per Acquisto Singolo; Inizia la tua avventura e ottieni Equipaggiamento Rosso!"

temp = "Free Self-choose Keys for Single Purchase; Start your adventure and get some Red Equipment!	Free Self-choose Keys for Single Purchase; Start your adventure and get some Red Equipment!	Clés de Sélection Gratuites pour un Achat Unique ; Commencez votre aventure et obtenez de l'Équipement Rouge !	Selbstgewählte Gratis-Schlüssel zum Einzelkauf; starte dein Abenteuer und erhalte einige Rote Ausrüstung!	Бесплатные ключи на выбор для одной покупки! Начните свое приключение и получите красное снаряжение!	Llaves de autoelección gratuitas para compra individual: ¡comienza tu aventura y consigue equipo rojo!	Free Self-choose Keys for Single Purchase; Start your adventure and get some Red Equipment!	Tek Satın Almaya Ücretsiz Kendin Seçmeli Anahtarlar: Macerana başla ve Kırmızı Ekipman kazan!	Free Self-choose Keys for Single Purchase; Start your adventure and get some Red Equipment!	Tasti di Scelta Automatica Gratuiti per Acquisto Singolo; Inizia la tua avventura e ottieni Equipaggiamento Rosso!"

result01 = hashlib.sha1(s.encode('UTF-8'))
result02 = hashlib.sha1(temp.encode('UTF-8'))

print(result01.hexdigest())
print(result02.hexdigest())
print(result01.hexdigest()==result02.hexdigest())

'''
百度翻译API

'''

# import http.client
# import hashlib
# import urllib
# import random
# import json
# import requests
# appid = '20200908000561487'  # 填写你的appid
# secretKey = 'O2xl7BlyZ3KaGYt8_X5Q'  # 填写你的密钥

# httpClient = None
# myurl = '/api/trans/胜利ip/translate'

# fromLang = 'auto'   #原文语种
# toLang = 'zh'   #译文语种
# salt = random.randint(32768, 65536)
# q= 'hello world'
# sign = appid + q + str(salt) + secretKey
# sign = hashlib.md5(sign.encode()).hexdigest()
# myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

# try:
#     results=requests.get('http://api.fanyi.baidu.com/api/trans/vip/translate'+myurl)

#     re = results.text
#     i = ast.literal_eval(re)
#     print(ast.literal_eval(i["trans_result"])["dst"])
# except Exception as e:
#     print (e)






'''
读取Excel文件
'''

# with xlrd.open_workbook("test.xls",encoding_override="UTF-8") as excel:
#     table = excel.sheets()[0]
#     nrows = table.nrows
#     ncols = table.ncols
#     i, j = 0, 0
#     result_list = []
#     for i in range(0, nrows):
#         for j in range(0, ncols):
#             cell = table.row_values(i)[j] #得到数字列数据
#             result_list.append(cell)
#     print(result_list)       


    # while i < nrows:
    #     while j < ncols:
    #         cell = table.row_values(i)[j] #得到数字列数据
    #         print(cell)
    #         j = j + 1
    #     i=i+1

        
        # print(cell)
    #     ctype = table.cell(i, 1).ctype #得到数字列数据的格式
    #     username=table.row_values(i)[0]
    #     if ctype == 2 and cell % 1 == 0: #判断是否是纯数字
    #         password= int(cell)  #是纯数字就转化位int类型
    #     print('用户名：%s'%username,'密码：%s'%password)
        


# file_name = xlrd.open_workbook("test.xls")
# table = file_name.sheets()[0]
# nrows = table.nrows
# ncols = table.ncols
# i = 0
# while i < nrows:
#     cell = table.row_values(i)[1]
#     print(cell)
#     i=i+1



# print(table)