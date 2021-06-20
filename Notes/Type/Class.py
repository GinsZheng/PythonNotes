# 类、构造函数、调用
class Dog():
    #构造函数
    def __init__(self, name, age):
        # 初始化属性
        self.name = name
        self.age = age
        self.color = "blue" #设定默认值时，可以不放入构造函数的参数
        self.steps_total = 0
        # 初始化的属性可以被所有函数使用
        # 初始化属性相当于直接定义了一个变量 self.xxx。

    def sit(self):
        print(self.name.title(), "is now sitting")  # 调用类的属性时也要加self

    def roll_over(self):
        print(self.name.title(),"rolled over")

    def getColor(self):
        print(self.name.title(), "is", self.color)

    def setColor(self, color):  # 通过函数修改属性值
        self.color = color
        print(self.name.title(), "is changed to", self.color)

    def increment_steps(self, steps):  # 通过方法对属性值递增
        self.steps_total += steps


# 调用
dog = Dog(name = "papy", age = 8)
dog.sit()

dog.color = 'red' # 修改属性的默认值
dog.getColor()
dog.setColor('green')
print(dog.color)

dog.increment_steps(10)  #递增调用
dog.increment_steps(100)
dog.increment_steps(200)
print("steps_total:", dog.steps_total)


# 继承、字义子类属性与方法、重写父类
class Doggy(Dog):  #继承放括号里

    fur = 'sparse'  #子类属性

    def __init__(self, name):
        self.color = "yellow"
        super().__init__(name, age = 0)

    def suckle(self):  #子类方法
        print(self.name.title(), "is suckling")

    def roll_over(self):  #重写父类
        print("rolling over is hard")


# 调用
doggy = Doggy("Little Yellow")
doggy.getColor()
doggy.suckle()
doggy.roll_over()


