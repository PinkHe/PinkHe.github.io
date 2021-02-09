import xlrd
import sys


# import DGUtils

sys.path.append("../..")
sys.path.append("..")

import DGUtils


excel_path = "DGame\D2GMAutoDemo\File\道具相关.xls"

props_dict = DGUtils.read_excel(excel_path)

print(props_dict)