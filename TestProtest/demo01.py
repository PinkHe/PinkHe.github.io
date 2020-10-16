'''
# 文件读写操作

Demo_file = open("test.text","r")
result_list = Demo_file.readlines()
result_list01 = []
for i in range(0,len(result_list)):
   result_list01.append(result_list[i].rstrip('\n'))
print(result_list01)

Demo_file.close()



s = 'hahahahh\n'
print(s.rstrip("\n"))

'''


'''
import pinyin

def getStrAllAplha(str):
    return pinyin.get_initial(str, delimiter="").upper()
    
def getStrFirstAplha(str):
    str=getStrAllAplha(str)
    str=str[0:1]
    return str.upper()
    

str = '你好在哪来'

print(getStrAllAplha(str))
print(getStrFirstAplha(str))

'''






#print("hellow python")





#模块
import ./../fibo

fibo.fib(10)
'''


#相关常用方法
当在字典中循环时，用 items() 方法可将关键字和对应的值同时取出
当在序列中循环时，用 enumerate() 函数可以将索引位置和其对应的值同时取出、
当同时在两个或更多序列中循环时，可以用 zip() 函数将其内元素一一匹配
如果要逆向循环一个序列，可以先正向定位序列，然后调用 reversed() 函数
如果要按某个指定顺序循环一个序列，可以用 sorted() 函数，它可以在不改动原序列的基础上返回一个新的排好序的序列
如果要按某个指定顺序循环一个序列，可以用 sorted() 函数，它可以在不改动原序列的基础上返回一个新的排好序的序列
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#dict()字典的构造函数
dict(a=22,b=44,c=66)
{x: x**2 for x in (2, 4, 6)}
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

student = {'name':'tom', 'age':12,'sex':'man'}

list01 = list(student)

print(student,"=========",list01)
print(student['name'])
print("=======================")
student['name'] = 'Marry'

print("=======================")
student['work'] = 'student'
print(student,"=========",list01)
print(student['name'])

#in/not in 检查字典中是否存在一个特定的键，返回布尔类型
print('man' in student)
'''


#列表推导式
#[表达式 for语句 (零个或多个if或者for语句)]
#列表推导式中的初始表达式可以是任何表达式，包括另一个列表推导式。
'''
[x*2 for x in range(6)]
print([x*2 for x in range(6) if x%2==0])

#collections中的deque可以很好的实现队列
from collections import deque

list01 = deque([1,2,3])

list01.appendleft(4)
list01.appendleft(5)

print(list01)

temp = list01.popleft()
print(temp)

print(list01)

#队列：先进先出(如下方法：效率很差，不推荐，推荐如上)
list01 = [1,2,3]
list01.insert(0,4)
list01.insert(0,5)
print(list01)

temp = list01.pop(0)
print(temp)

print(list01)


#堆栈：先进后出
stack = [1,2,3,4]


stack.append(6)
print(stack)
stack.append(7)
print(stack)
temp = stack.pop()
print(temp)
print(stack)
'''
'''
()  元组
[]  列表
{}  字典


list01 = ["111","123","333"]

list02 = ["444","555","666"]

list02.append("777")
#list02.extend(list01)
list02[len(list02):] = list01
print(list02)

#后两个可选参数是切片参数，表示在列表中的那个切片中寻找
index = list02.index("333",0,len(list02))
print(index)
#list02.sort()
#翻转列表中的元素
list02.reverse()
print(list02)
'''
#lambda表达式：i:i+2 注：i即为函数入口参数，i+2即为函数体；lambda表达式的意义为简化简单函数的定义
'''
def fun(x):
    return lambda i:i+2

f = fun(7)
print(f(1))


def f(a, L=None):
    if L is None:
        L = []
    print(L)
    L.append(a)
    return L

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
'''

'''
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('')
'''
#函数打印乘法表
#print(end="")即可不换行输出
'''
def fun():
    for i in range(1,10):
        for j in range(1,i+1):
            print(j,"*",i,"=",i*j,end=" ")
        print()

fun()
'''
#函数
'''
def fib(n):
    num = []
    a , b =0 , 1
    while a < n:
        num.append(a)
        a, b = b, a+b
    return num

print(fib(100))
'''
'''
num = 0
for i in range(1,100,2):
    if i == 1 or i == 3 or i == 5:
        if i==1:
            continue
        else:
            num.append(i)
    else:
        if i%3 != 0 :
            if i%5 != 0 :
                num.append(i)
            else:
                continue
        else:
            continue
num.insert(0,2)
print(num)

'''
#pass 语句什么也不做。当语法上需要一个语句，但程序需要什么动作也不做时，可以使用它---通常用于创建最小的类
#循环中的 else 子句则会在未发生 break 时执行,break跳出最近的一个循环(for、while)
#continue 语句表示继续循环中的下一次迭代:
'''
temp = 0
for i in range(2,100):
    
    for j in range(2,i):
        if i%j == 0 :
            break
    else:
        temp = temp+1

print(temp)
'''

#质数（素数）：大于一的自然数，只能被1和本身整除

# num = []
'''
for i in range(2,499979):
    temp = 0
    for j in range(1,i+1):
        if i%j == 0 :
            temp=temp+1
    if temp==2:
        num.append(i)
 
print(num)
'''

# 2、3、5、7、11、13、17、19、23、29、31、37、41、43、47、53、59、61、67、71、73、79、83、89、97
# 2、3、5、7、11、13、17、19、23、29、31、37、41、43、47、53、59、61、67、71、73、79、83、89、97

#for、if-else

#在for循环中如果会对列表中的数据进行改变则在循环条件中用切片
#range()函数：一个可以生成指定开始和增幅的顺序列表，增幅即为“步进”
#range()函数虽然表现的是一个完整的列表，但是其内部为节省空间，只会存储关键信息，即起点、终点和步进，完整的列表元素是在运行中生成的
'''
for i in range(1,6,2):
    print(i)
'''


'''
words = ['ddd','cccc','bbb','aaa']
i=0;
for w in words[:]:
    ++i
    print(i,w)
    if len(w)>3 :
        words.insert(0,w)
        

print(words)
'''

# while---斐波拉切数列
'''
a , b = 0 , 1
array = []
while a < 1000 :
    array.append(a)
    a , b = b , a + b
print(array)
'''

# 简单输入输出

'''
people = {}
name = input("name:")
age = input("age:")
sex = input("sex:")

#people.keys("name"=name)
#people.keys("age"=age)
#people.keys("sex"=sex)

people.update(name=name)
people.update(age=age)
people.update(sex=sex)

people

print(people)
'''


# hello Python

'''
a = (1,2,3,4,'杨狗狗','杨猫猫','杨猪猪')

print(a.index("杨狗狗"))
print(a.count(1))

'''


'''
str1 = input()
str2 = input()

print(str1)

print("输入的两段和为:",len(str1)+len(str2))

'''

