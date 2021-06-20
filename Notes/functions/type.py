# type() 获取数据类型
L = ['a','b','c']
print("获取数据类型", type(L))

# 判断函数类型方法1
if type(L) == list:
    print("yes")

# 判断函数类型方法2
if isinstance(L, list):
    print("yes")