s = ['(1,2)','(1,3)','(1,4)','(1,5)','(1,6)']

a = ['(1,2)','(1,3)','(1,4)']


for i in s:
     if i in a:
          s.remove(i)
print(s)