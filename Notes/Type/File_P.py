# 文件操作

# open() 打开：即读取文件。先打开，才有后续的操作
F = open('/Users/GinsMac/Downloads/Gins/Software/Library/lib_PyCharm/PythonNotes/sources/aFewLines.txt')

# next()逐行读取内容，
print(next(F))
print(next(F))
print(next(F))

# 输出结果保存到文件-
