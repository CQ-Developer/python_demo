import json

nums = [1, 2, 3, 4, 5]
filename = "nums.json"

# 将json数据写入文件中
with open(filename, "w") as f:
    json.dump(nums, f)

# 从json文件中读取数据
with open(filename) as f:
    print(f.read())
