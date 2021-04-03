# range() 生成一个范围内的数值
nums = range(1, 5)
for num in nums:
    print(num) # ➤ 1 2 3 4 (4行)
    # range 返回一个序列，但不是数组，前闭后开区间

# range转为数组
nums = list(range(1, 5))
print('rangeToList ➤ ', nums)

# range 指定步长(参数3)
nums2 = range(1, 10, 2)
print('range step ➤ ', list(nums2))

