#zip()：取得一个或多个序列为参数，然后返回元组的列表，将序列中并排的元素配成对。
L1 = [1,2,3,4,5,6]
L2 = [5,6,7,8]
print("zip基本用法 ➤ ", list(zip(L1,L2))) # 把L1与L2的并排元素配对,而无法配对的，则移除

# zip可接受接受任何类型的序列(即任何可迭代的对象)，包括文件
# zip返回可迭代对象

#zip遍历
L1 = [1,2,3,4]
L2 = [5,6,7,8]
for (x, y) in zip(L1, L2):
    print('%d + %d = %d' % (x,y,x+y))
    # 1 + 5 = 6 ……  | 相当于传入两个参数

#zip构造字典
keys = ['name', 'age']
vals = ['Gins', '25']
D = dict(zip(keys, vals))
print("#zip构造字典 ➤ ", D)