filename = "pi_digits.txt"

# 读取文件内容并将其打印到控制台
# with 类似与 Java 中的 try-with-resource 可以自动关闭资源
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

# 逐行打印文件内容
with open(filename) as file_object:
    for content in file_object:
        print(content.rstrip())
