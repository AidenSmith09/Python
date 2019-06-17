# /bin/etc/env Python
# -*- coding: utf-8 -*-
def build_person(first_name_person, last_name_person, age=''):
    person = {'first': first_name_person, 'last': last_name_person}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix',age = 12)
print(musician)
"""
将数据返回到字典中去做存储。
age = '' 即为空，当传参无此数据的时候，字典不进行保存。
"""

"""
结合while循环写一个问候语
"""
def get_formatted_name(first_name, last_name):
    full_name =  first_name + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if f_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

"""
传递列表
假设有一个用户列表，要问候其中每个用户。
可以做用户推送，如根据user表的主键进行遍历。
"""
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hanah', 'trt', 'margot' , 'mongodb']
greet_users(usernames)