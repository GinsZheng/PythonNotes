bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print('list ➤ ', bicycles)
print('an element of list ➤ ', bicycles[2])

# 最后一个元素 
print('last element ➤ ', bicycles[-1])

# 增(尾部)
bicycles.append('giant')
print('append ➤ ', bicycles)
# 增(任意位置)
bicycles.insert(2, 'phoenix') # 原本在索引2之后的内容整体向后移
print('insert ➤ ', bicycles)


# 删(可继续使用，按索引删除)
lastElement = bicycles.pop() #pop之后，赋值后可以继续使用。pop不加参数为删除最后一元素
print('pop ➤ ', bicycles)
print('lastElement ➤ ', lastElement)
firstElement = bicycles.pop(0)
print('pop(0) ➤ ', bicycles) #pop(0)可删除任意位置
# 删(不可继续使用，按索引删除)
del bicycles[2] #del之后，无法继续使用(与pop不同)
print('del ➤ ', bicycles)
# 删(按值删除)
bicycles.remove('phoenix') #remove的值，如果出现多次，只删除第一个。可循环删除所有
print('remove ➤ ', bicycles)

# 改
bicycles[0] = 'mereda'
print('update ➤ ', bicycles)

# 多类型
pythonList = [1, '10', 'string', (1, 3)]
print(pythonList[3])

# 切片 Slices
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print('slices ➤ ', bicycles[1:3])
    #前闭后开区间
print('slices only right ➤ ', bicycles[:3])
    #单边区间时：左单向为从[0:n], 右单向为[n:最后]
print('slices with - ➤ ', bicycles[1: -1])
    #-1代表最后一个，此例取第2个到倒数第二个
print('slices with -(2) ➤ ', bicycles[-2:])
    #此例取最后两个
anotherBicycles = bicycles[:]
print('slices as copy ➤ ', anotherBicycles)
    #用于复制一个数组




















