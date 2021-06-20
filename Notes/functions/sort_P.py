# 排序

# 永久排序 sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #所有点调用⌜xx.sort()⌟的都是永久处理
print('sort ➤ ', cars)

# 临时排序 sorted
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
sorted(cars2) #所有内置函数⌜sorted(xx)⌟都是临时处理，通常以赋值的方式改为永久处理
print('sorted 临时处理 ➤ ', sorted(cars2))
print('sorted 恢复原状 ➤ ', cars2)
cars2 = sorted(cars2)
print("赋值后永久化", cars2)

# 永久倒序
cars.reverse()
print('reverse ➤ ', cars)

# 有key的排序  
L = ['abc', 'aBe', 'ABD']
L.sort(key=str.lower)  # 将字母全转成再排序  
print("有key的排序", L) # ➤ ['ABD', 'aBe', 'abc']  
