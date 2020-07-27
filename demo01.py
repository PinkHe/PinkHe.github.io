
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

