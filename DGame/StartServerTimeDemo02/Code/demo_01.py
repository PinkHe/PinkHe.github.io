import re

import sys
sys.path.append("..")
sys.path.append("../..")

import DGUtils

path = "SetFile/eg.xls"

list01 = DGUtils.read_excel(path)
# listStr = str(list01)

# list02 = listStr.split("活动")

for i in range(0,len(list01)):
    # list01[i] = re.sub(r'活动[0-9]+',"分割线",str(list01[i]))
    if len(re.findall(r'活动[0-9]+',str(list01[i]))) > 0:
        list01.insert(i, "==================") 

    
    # print(i)
# list02 = re.split("分割线", str(list01))
# for i in list02:
#     print(i)

for i in list01:
    print(i)