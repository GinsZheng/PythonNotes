# 普通函数
price = 0
def getPrice(age): #定义
    if age<18:
        price = 5
    else:
        price = 10
    print("# 普通函数", price)
getPrice(10) #调用
# 形参与实参：上例中，age为形参，10为实参


# 参数设默认值
def getPrice2(age=20):
    if age<18:
        price = 5
    else:
        price = 10
    print("# 参数设默认值", price)
getPrice2()


# 任意数量的参数
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


# 位置实参与关键字实参
def getPrice5(name, age):
    print("名字", name, ", 年龄", age)
getPrice5("Gins", 30) #位置实参：以位置传参，按顺序传参
getPrice5(age = 30, name = "Gins") #关键词实参，无需考虑顺序
getPrice5("Gins", age = 30) #混合实参













