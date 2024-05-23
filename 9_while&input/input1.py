# 使用 input 接收用户的输入
msg = input("input your age: ")
print(f"your age is {msg}")

# 使用 int 将用户输入转化为数字
age = int(msg)

if age > 18:
    print("you can join game")
else:
    print("you are too young")
