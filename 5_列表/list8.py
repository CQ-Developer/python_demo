nums = [v for v in range(1, 11)]

# 切片：取列表的第 2-5 个元素
print(nums[1:5])

# 切片：取列表的前3个元素
print(nums[:3])

# 切片：取列表的第 4-end 个元素
print(nums[3:])

# 切片：取列表的后3个元素
print(nums[-3:])

# 切片：从 2-8 每隔一个取一个
print(nums[1:8:2])

# 切片：每隔一个元素取一个
print(nums[0::2])

# 切片：赋值列表
copied_nums = nums[:]
copied_nums.append(11)
print(nums, copied_nums)
