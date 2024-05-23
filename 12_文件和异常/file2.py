# 计算文件包含多少个单词
filename = "file2.py"

try:
    with open(filename, encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    words = content.split()
    nums_words = len(words)
    print(f"The file {filename} has about {nums_words} words.")
