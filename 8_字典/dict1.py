# 定义字典
person = {
    "name": "Jack",
    "age": 18
}

# 读取字典
name = person["name"]
print(name)

# 修改字典
person["age"] = 20
print(person["age"])

# 添加值
person["address"] = "China"
print(person["address"])

# 访问不存在的值报错
# print(person["gender"])

# 使用 get 进行安全的访问
gender = person.get("gender")
print(gender)

# 使用 get 并提默认值
gender = person.get("gender", "unknown")
print(gender)
