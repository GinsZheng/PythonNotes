# While基础
i = 0
numbers = []
while i < 6:
    numbers.append(i)
    i += 1
print("While基础", numbers)


# continue 跳到下一个循环(不执行continue之后的代码，直接开始下一个循环)
x = 10
while x:
    x = x - 1
    if x % 2 != 0: # 判断是否为非偶数，是则直接开始下一个循环，而不执行下面的print
        continue
    print(x, end=' ') # ➤ 8 6 4 2 0
print() #用于换行


# 使用标志退出循环
active = True
x = 0
while active:
    x += 1

    if x > 3:
        active = False
    else:
        print("使用标志", x)


# pass 空占位语句(什么事都不做，仅占位，用于不能为空的情况，如：只写「if a == 1:」会报错)
x = 4
while x:
    x = x - 1
    if x == 3:
        print("x大于3")
    else:
        pass #示意，pass有时用于“以后会填上”的情况


# else 循环中的else，当循环正常结束时执行(未被break)
def isPrime(n): #判断是质数还是合数
    x = n // 2
    while x > 1:
        if n % x == 0:
            print(n, 'has factor', x)
            break
        x -= 1
    else:
        print(n, 'is prime')
        # else为Python特有，其他语言需要标志位(即先设 x = False，
        # if某某条件为真，则x = True。然后再独立写一条判断：if x == True，……)
isPrime(9)


# break 跳出循环
while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    print(reply.upper())
    # 如果多个循环嵌套，只会跳出对应的那一个循环，而不是整个循环