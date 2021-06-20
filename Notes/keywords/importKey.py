import random  # 导入模块
from sys import exit  # 导入模块中特定函数
import importedModule  # 导入自定义模块(同一个目录中)
from importedModule import getPrice, getColor  # 导入自定义模块中特定函数
import importedModule as IM  #导出模块并重命名模块
from importedModule import getColor as GC #导出模块并重命名函数
from importedModule import * #导入所有函数


price = importedModule.getPrice(10) #调用：导入模块时，需要前缀
price2 = getPrice(20)
price3 = IM.getPrice(30) #调用：导出模块并重命名模块的
price4 = GC(40)
price5 = getColor("blue")  #调用时无需前缀

