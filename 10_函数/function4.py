def build_profile(first, last, **user_info):
    """
    测试任意数量的关键字实参
    :param first: 名
    :param last: 姓
    :param user_info: 用户信息，本质是一个字典
    :return: 用户信息
    """
    print(user_info, type(user_info))
    user_info[first] = first
    user_info[last] = last
    return user_info


user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)
