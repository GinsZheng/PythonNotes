import random  # 导入模块
from sys import exit  # 导入模块中特定函数
import importedModule_P  # 导入自定义模块(同一个目录中)
from importedModule_P import getPrice, getColor  # 导入自定义模块中特定函数
import importedModule_P as IM  #导出模块并重命名模块
from importedModule_P import getColor as GC #导出模块并重命名函数
from importedModule_P import * #导入所有函数

# 调用
price = importedModule_P.getPrice(10) #调用：导入模块时，需要前缀
price2 = getPrice(20)
price3 = IM.getPrice(30) #调用：导出模块并重命名模块的
price4 = GC(40)
price5 = getColor("blue")  #调用时无需前缀


# 相对路径导入
import sys
sys.path.append("../Type")  #把相对路径加入环境变量
from Class_P import Dog  #导入类

#相对路径调用
c = Dog("pipa", 2)
c.sit()


"""
import说明：
import 的搜索路径：
▸ 在当前目录下搜索该模块
▸ 在环境变量 PYTHONPATH 中指定的路径列表中依次搜索
▸ 在 Python 安装路径的 lib 库中搜索
"""
