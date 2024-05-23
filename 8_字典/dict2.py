favorite_language = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

# 遍历键值对
for k, v in favorite_language.items():
    print(f"{k.title()}'s favorite language is {v}")

# 遍历键：keys() 可以省略
for k in favorite_language.keys():
    print(k)

# 判断是否在字典中
name = "jack"
if name not in favorite_language.keys():
    print(f"{name} not on list")

# 按指定顺序遍历
for k in sorted(favorite_language.keys()):
    print(f"{k.title()}'s favorite language is {favorite_language[k]}")

# 遍历值
for v in favorite_language.values():
    print(v)

# 遍历值时使用 set 集合去重
for v in set(favorite_language.values()):
    print(v)
