"""
如果用户第一次登录，保存用户名
否则和用户打招呼
"""

import json


def save_username(username, filename):
    """存储用户名"""
    with open(filename, "w") as f:
        json.dump(username, f)
        print(f"Hey {username}, I'll remember you.")


def load_username(filename):
    """加载用户名"""
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        return None


def greet_user():
    """打招呼"""
    filename = "username.json"
    username = load_username(filename)
    if username:
        print(f"Welcome back {username}!")
    else:
        save_username(input("Type your name please, I'll remember you: "), filename)


# 调用方法
greet_user()
