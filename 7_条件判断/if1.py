# 买票
age = 20

if age <= 5:
    print("免票")
elif age < 23:
    print("半票")
elif age < 60:
    print("全票")
else:
    print("免票")

# 判断元素是否在列表中
nums = [i for i in range(10)]

if 5 in nums:
    print("5 in nums")

if 10 not in nums:
    print("10 not in nums")

# and
if 1 in nums and 5 in nums:
    print("1 and 5 in nums")

# or
if 1 in nums or 10 in nums:
    print("1 or 10 in nums")
