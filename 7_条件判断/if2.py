# 点披萨
toppings = ["芝士", "香肠", "蘑菇酱"]

# if 可以直接判断列表是否位空
if toppings:
    for topping in toppings:
        print(f"Adding {topping}")
    print("\nFinish making pizza!")
else:
    print("Are you sure you want a plain pizza")
