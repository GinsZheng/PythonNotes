# filter(func, iter)
# filter过滤内容，函数返回True的留下，False的去掉

x = filter((lambda x: x > 0), range(-5, 5))
print(list(x))