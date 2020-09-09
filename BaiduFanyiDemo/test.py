import xlrd

with xlrd.open_workbook("test.xls",encoding_override="UTF-8") as excel:
    table = excel.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    i = 0
    while i < nrows:
        cell = table.row_values(i)[1] #得到数字列数据
        print(cell)
    #     ctype = table.cell(i, 1).ctype #得到数字列数据的格式
    #     username=table.row_values(i)[0]
    #     if ctype == 2 and cell % 1 == 0: #判断是否是纯数字
    #         password= int(cell)  #是纯数字就转化位int类型
    #     print('用户名：%s'%username,'密码：%s'%password)
        i=i+1


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