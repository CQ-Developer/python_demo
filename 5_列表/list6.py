# 创建 1-10 的平方数列表
nums = []
for i in range(1, 11):
    nums.append(i ** 2)
print(nums)

# 使用列表解析
nums = [v ** 2 for v in range(1, 11)]
print(nums)
