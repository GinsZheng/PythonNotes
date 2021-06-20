# 将数组下标与序列值组成元组，并形成新数据
S = 'spam'
for (offset, item) in enumerate(S):
    print(item,'at offset', offset)

# next()调用
S = 'spam'
print(enumerate(S))
print(list(enumerate(S))) # ➤ [(0, 's'), (1, 'p'), (2, 'a'), (3, 'm')]
E = enumerate(S)
print(next(E))
print(next(E))
print(next(E))
print(next(E)) # 如果所有的元组都调用完了，会报错