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

# Change Function List
# 未使用函数的代码
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 使用过后的数据，移动至 completed_models 列表中
while unprinted_designs:
    current_design = unprinted_designs.pop()  # 删除列表中最后一个数据，并存储变量

    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_models in completed_models:
    print(completed_models.title())


# 使用函数重组代码，对比其区别。
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()  # 删除列表中最后一个数据，并存储变量
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_models in completed_models:
        print(completed_models.title())

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

# 第二种写法更加直观，创建函数后，它不用去管数据是什么，仅对行为做操作。
# 虽然两种写法结果都一样，但理念是不同的。
# 即每个函数只负责一项具体的工作，不需要管理其他的事物。
# 这种写法在排错上也更加容易定位问题。
# 且在修改代码上，不需要进行全局操作。仅仅修改一个函数即可。
