# 把字符串转换为可执行代码

myFile = open('/Users/GinsMac/Downloads/Gins/Software/Library/lib_PyCharm/PythonNotes/sources/list.txt') # 'data.txt'中内容为：[1,2,3]
line = myFile.readline()
print(line) # ➤ '[1,2,3]' | 字符串
print(eval(line)) # ➤ [1, 2, 3] | 把字符串转为列表

L = eval(line)