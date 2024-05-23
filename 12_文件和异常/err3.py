"""
静默失败：
使用 pass 关键字让 Python 捕获异常时，将什么都不做
"""

filename = "alice.txt"

try:
    with open(filename, encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    pass
