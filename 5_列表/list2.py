cars = ['bmw', 'audi', 'toyota', 'subaru']
# 正序
cars.sort()
print(cars)
# 倒序
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
# 正序，不改变原列表
ordered = sorted(cars)
print(cars, ordered)
# 倒叙序，不改变原列表
ordered = sorted(cars, reverse=True)
print(cars, ordered)

cars = ['bmw', 'audi', 'toyota', 'subaru']
# 反转列表
cars.reverse()
print(cars, cars)
