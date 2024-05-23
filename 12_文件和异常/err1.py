# 将会出先错的代码放入try中
# 用expect捕获异常进行处理
# 用else块执行正确结果

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    a = input("\nFirst number: ")
    if a == 'q':
        break
    b = input("Second number: ")
    if b == 'q':
        break
    try:
        ans = float(a) / float(b)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(ans)
