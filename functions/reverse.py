#反转顺序

#永久反转
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print("永久反转", cars)

#临时反转
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
list(reversed(cars2)) #reversed()必须包装在一个list调用中，因为它是一个迭代器
print("临时反转(此处不反转)", cars2)
print(list(reversed(cars2)))

