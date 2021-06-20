# split(x)字符串拆分
line = 'aaa,bbb,ccccc,dd'
print("split ➤ ", line.split(',')) # ➤ ['aaa', 'bbb', 'ccccc', 'dd'] | 以逗号为分隔符。

# join(x)列表合成为字符串
x = ['A', 'r', 'e', ' ', 'y', 'o', 'u', ' ', 'O', 'K', '?']
y = "".join(x)
print("join ➤ ", y)
y = ",".join(x) #以逗号合成列表为一个字符串
print("join ➤ ", y)

#大小写
x = 'Spam'
print(x.upper()) # ——➤ SPAM
print(x.lower()) # ——➤ spam

#布尔判断
x = 'Spam'
print(x.isalpha()) # ——➤ True | 检测字符串是否只由字母组成
z = '123'
print(z.isdigit()) # ——➤ True | 检测字符串是否只由数字组成

#移除空白符
line = 'aaa,bbb,ccccc,dd\n\n\n'
print(line.rstrip()) # 去掉右边的三个空白符(此处为换行符)
print(line.lstrip()) # 左边
print(line.strip()) # 两边

#首尾匹配
x = 'Are you OK?'
print(x.startswith('Are')) # ——➤ True
print(x.endswith('OK?')) # ——➤ True

#抑制转义(r"")
s = r'a\n\tbc'
print("抑制转义", s)

#ASCII转换
print(ord('A')) # ——➤ 65
print(chr(65)) # ——➤ A
print(chr(ord('a')+3)) # ——➤ d

