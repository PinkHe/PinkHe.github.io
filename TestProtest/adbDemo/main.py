import os

adb = "adb devices"

text = os.system(adb) 
print(text)