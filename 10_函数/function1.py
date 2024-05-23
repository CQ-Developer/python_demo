# 定义函数
# 为形参指定默认值
def desc_pet(pet_name, animal_type="dog"):
    print(f"\nI have a {animal_type}")
    print(f"It's name is {pet_name}")


# 调用函数
desc_pet("jack")

# 通过形参顺序调用函数
desc_pet("jerry", "mouse")

# 通过关键字传递参数
desc_pet(pet_name="tom", animal_type="cat")
