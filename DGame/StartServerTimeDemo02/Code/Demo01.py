import re

import sys
sys.path.append("..")
sys.path.append("../..")

import DGUtils

path = "SetFile/eg.xls"

list01 = DGUtils.read_excel(path)
# listStr = str(list01)

# list02 = listStr.split("活动")

for i in list01:
    print(re.sub(r'活动(.*)',"分割线",str(i)))
    # print(i)