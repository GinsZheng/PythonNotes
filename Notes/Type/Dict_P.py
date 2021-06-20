# 字典没有顺序，所以合并两个字典时，没有固定顺序，输出字典时，也不会按输入的顺序排列  

# 创建字典
D = {}  #空字典
D2 = {'name': 'Gins', 'age': 25}  #非空字典
D3 = dict.fromkeys(['a', 'b'], 1)  #通过列表创建
print("D, D2, D3:", D, D2, D3)


#  通过列表创建键值对
L1 = ['a', 'b', 'c']
L2 = ['Are', 'you', 'OK?']
D4 = dict(zip(L1, L2)) # L1为键，L2为值
print("D4:", D4)


# 调用
print("调用",D2['name'])


# 新增/修改
D2['sex'] = "Male"
print('新增', D2['sex'])
D2['name'] = 'Ryes'
print("修改", D2['name'])


# 删除
del D2['sex']
print("删除", D2)


# 删除键并返回其值 pop
V1 = D2.pop('age')
print("pop返回值", V1)
print("pop后的字典", D2)


# 字典值(有值时)获取或(无值时)返回设定值
print(D2.get('born', 1993)) #注，不会新增值


# 合并字典
D2.update(D3)
print("D2", D2)


# 键的排序
D5 = {'a':1, 'c':3, 'b':2}
print('D5', D5)
for key in sorted(D5):
    print(key, '->', D5[key])


# 获取键/值列表
print('键', list(D5.keys()))
print('值', list(D5.values()))

