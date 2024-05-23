# 列表
letters = ["a", "b", "c", "d"]

# 访问第一个元素
print(letters[0])

# 访问列表元素并执行操作
print(letters[1].upper())

# 反向访问列表元素
print(letters[-1])
print(letters[-2])

# 在列表末尾添加元素
letters.append("e")
print(letters)

# 弹出列表末尾元素
letter = letters.pop()
print(letter)
print(letters)

# 在指定位置插入元素
letters.insert(0, "A")
print(letters)

# 删除指定位置的元素
del letters[0]
print(letters)

# 弹出指定位置元素
letters.pop(0)
print(letters)

# 删除指定值
letters.remove("c")
print(letters)

# 获取列表元素数量
letters_len = len(letters)
print(letters_len)
