print("hello Python world!")

# 字符串大写
msg = "abc"
print(msg.upper())

# 字符串小写
msg = "ABC"
print(msg.lower())

# 单词首字母大写
msg = "chen qiang"
print(msg.title())

# 去除字符串右侧空白字符
msg = "python   "
print(msg.rstrip())

# 去除字符串左侧空白字符
msg = "   python"
print(msg.lstrip())

# 去除字符串两边空白字符
msg = "   python   "
print(msg.strip())

# 使用format进行格式化
first_name = "qiang"
last_name = "chen"
print("{} {}".format(first_name, last_name))

# 使用f字符串进行格式化 python3.6+
first_name = "qiang"
last_name = "chen"
print(f"{first_name} {last_name}")

# 使用replace替换字符串内容
content = "abc"
print(content.replace("b", "o"))
