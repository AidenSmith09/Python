# /bin/etc/env Python
# -*- coding: utf-8 -*-
import json

# 第三次剥离
# 加载文件，只做加载
# 写入文件，只做写入
# 最后输出时，做一个判断。username带参则输出，不带参，则执行另一个函数。
def get_stored_username():
    filename = "username.json"
    try:
        with open(filename)as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("你的名字：")
    filename = "username.json"
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()  #首先加载文件后，赋值
    if username: # 判断username是否带参
        print("欢迎回来" + username + "！")
    else: # 不带参
        username = get_new_username() #不带参则执行次函数
        print("我们会记住你的" + username + "！")


greet_user()

#第二次编写
#加载文件内容做成一个函数
#写入文件作为一个函数。但在写入之前先做判断，文件内是否有内容。
"""
def get_stored_username():
    filename = "username.json"
    try:
        with open(filename)as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_username()
    if username:
        print("欢迎回来" + username + "！")
    else:
        username = input("你的名字：")
        filename = "username.json"
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("我们会记住你的" + username + "！")

greet_user()
"""


# 第一次编写
# 代码看着很混乱，各种功能混杂在一起。
# 有读取文件并加载，判断没有内容后，做输入。然后再做输出。
"""

filename = "username.json"

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("你的名字：")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("我们会记住你的"+username+"！")
else:
    print("欢迎回来"+username+"！")
"""
