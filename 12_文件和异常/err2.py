# 处理FileNotFoundError
filename = "alice.txt"

try:
    with open(filename, encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
