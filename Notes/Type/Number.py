# 进制
x = 0xff
print("十六进制", x) # ➤ 255 | 十六进制
x = 0o77
print("八进制", x) # ➤ 63 | 八进制
x = 0b1001
print("二进制", x) # ➤ 9 | 二进制


# 进制转换
print(hex(255)) # ➤ 0xff
print(oct(255)) # ➤ 0o377
print(bin(255)) # ➤ 0b11111111


#类型转换
x = 100.3
print("int", int(x))
x = "100"
print("int", int(x))
x = "100.3"
print("int", int(float(x))) # 直接int(x)，会报错
x = "0xff"
print("进行转换", int(x, 16)) # 16指16进制

x = "100"
print("float", float(x))
print("list", list(x))

x = 100
print("str", str(x))
# 类似的的还有 dict(x) / tuple(x) / set(x)

#数值自动转换
x = 3
y = 4.5
print("数值自动转换", x + y) #自动升级为更复杂的类型(复杂度：整数<浮点<复数)

