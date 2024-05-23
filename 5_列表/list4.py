# range 1个参数
for v in range(10):
    print(v)

# range 2个参数
for v in range(5, 10):
    print(v)

# range 3个参数
for v in range(1, 10, 2):
    print(v)

# 生成 1-10 列表
nums = list(range(1, 11))
print(nums)

# 生成 1-10 的偶数列表
nums = list(range(2, 11, 2))
print(nums)

# 生成 1-10 平方的列表
nums = []
for v in range(1, 11):
    nums.append(v ** 2)
print(nums)
