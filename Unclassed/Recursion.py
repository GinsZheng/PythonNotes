#递归

#栗子：列表求和
def mysum(L):
    if not L: # L为空时返回True
        return 0
    else: # L非空时，执行此句
        return L[0] + mysum(L[1:]) # call myself(调用自己)，然后又开始一遍mysum()函数
print("列表求和", mysum([1,2,3,4,5]))


"""递归工作原理：
▸ print(mysum([1,2])) ➤ 3
▸ mysum([1,2]),返回 L[0] + mysum(L[1:])，即 1 + mysum([2])
▸ mysum([2]),返回 L[0] + mysum(L[1:])，即 2 + mysum([])
▸ mysum([]),返回 0
▸ 然后返推：mysum([2])，返回 2 + mysum([]) = 2 + 0 = 2
▸ 再返推：mysum([1,2])，返回 1 + mysum([2]) = 1 + 2 = 3
"""


#栗子2：任意嵌套列表数值求和
def sumtree(L):
    total = 0
    for x in L:
        if not isinstance(x,list):
            total += x
        else:
            total += sumtree(x)
    return total
L = [1, [2, [3, 4], 5], 6, [7, 8]]
print("任意嵌套列表数值求和", sumtree(L))


#栗子3：输出斐波那契数列第n位数
def getFibonacci(n):
    if n <= 2:
        return 1
    else:
        return getFibonacci(n-1) + getFibonacci(n-2)
print("斐波那契数列", getFibonacci(10))


#栗子4：求阶乘
def factorial(n):
    if n == 1:
        return n
    return n*factorial(n-1)
res = factorial(n = 5)
print("求阶乘", res)






