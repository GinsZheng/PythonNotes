# 普通函数
price = 0
def getPrice(age): #定义
    if age<18:
        price = 5
    else:
        price = 10
    print("# 普通函数", price)
getPrice(10) #调用

# 参数设默认值
def getPrice2(age = 20):
    if age<18:
        price = 5
    else:
        price = 10
    print("# 参数设默认值", price)
getPrice2()

# 参数为数组/元组
def getPrice3(*ageArray):
    for x in ageArray:
        print("# 参数为数组/元组", x)
getPrice3(10,20,30,"hey")

#参数为字典
def getPrice4(**list):
    for x in list:
        print("# 参数为字典", x)
dic = {"name": "Gins", "age": 20}
getPrice4(**dic)




















