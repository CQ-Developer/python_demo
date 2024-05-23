"""使用标准库"""

from random import randint
from random import choice

# 生成10次1-100之间的随机数
for i in range(10):
    print(randint(1, 101))

# 在1-100的列表中随机选择一个数10次
nums = [i for i in range(1, 101)]
for i in range(10):
    print(choice(nums))
