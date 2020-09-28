# -- coding ➤ utf-8 --

Sum = sum([1,2,4,5])

Pow = pow(1,3)

Abs = abs(-10)

Min = min(1,2,3)

Max = max(1,2,3)

Any = any(['spam', '', '3'])
print('any ➤ %r' % Any) # 或运算，有一个值为真就返回True

All = all(['spam', '', '3'])
print('all ➤ %r' % All) # 与运算，有一个值为假就返回False

Round = round(0.51)
print('round ➤ %r' % Round) #四舍五入。注：精度要求高时，导入 decimal 模块处理
Round2 = round(56.659, 1)
print('round2 ➤ %r' % Round2) #四舍五入到特定小数位(参数2：小数位)
