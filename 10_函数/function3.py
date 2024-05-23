def print_nums(*nums):
    """
    测试任意数量的实参
    :param nums: 数字，本质上一个元组
    :return: None
    """
    for num in nums:
        print(num)


# 调用函数
print_nums(1, 2, 3)
print_nums(4, 5, 6, 7, 8, 9, 10)
