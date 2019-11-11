# /bin/etc/env Python
# -*- coding: utf-8 -*-
def build_person(first_name_person, last_name_person, age=''):
    person = {'first': first_name_person, 'last': last_name_person}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age = 12)
print(musician)
"""
将数据返回到字典中去做存储。
age = '' 即为空，当传参无此数据的时候，字典不进行保存。
"""

"""
结合while循环写一个问候语
"""


def get_formatted_name(first_name, last_name):
    full_name = first_name + last_name
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


usernames = ['hanah', 'trt', 'margot', 'mongodb']
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
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# 第二种写法更加直观，创建函数后，它不用去管数据是什么，仅对行为做操作。
# 虽然两种写法结果都一样，但理念是不同的。
# 即每个函数只负责一项具体的工作，不需要管理其他的事物。
# 这种写法在排错上也更加容易定位问题。
# 且在修改代码上，不需要进行全局操作。仅仅修改一个函数即可。

# 传递任意数量的实际参数
def make_pizza(*topings):  # 星号的作用是创建一个空元组
    print("\nMaking a pizza with the following topings:")
    for topings in topings:
        print("- " + topings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 使用位置实参和任意数量实参
def make_pizza_2(size, *toppints):
    print("\nMaking a " + str(size) + "- inch pizza with the following toppings:")
    for topping in toppints:
        print("- " + topping)

make_pizza_2(16, 'pepperoni')
make_pizza_2(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
可以发现，12被存储在size中，单剩下的字符串却被存储在元组toppings中。
'''
print("------分割线-------")


def build_profile(first, last, **user_info):  # 其实可以理解为，第一个为形参，第二个为形参，第三则为字典形参；双星号表示创建一个空字典。
    profile = {}  # 创建一个字典用于保存字典形参
    profile['first_name'] = first  # 保存第一个形参
    profile['last_name'] = last  # 保存第二个形参
    for key, value in user_info.items():  # 循环参数中传入的的键值对，并进行存储。
        profile[key] = value  # 此处的表现形式不理解
    return profile  # 返回数据至profile
user_profile = build_profile('albert', 'einstenin', location='princeton', field='physics')  # 第三、四个参数是一个整体，作为字典参数。
print(user_profile)  # 输出最终结果。
print("------分割线-------")

"""
函数变量作用域
函数内部的变量称之为局部变量，不允许被外部调用，一旦函数执行完毕局部变量就会被回收。
函数外部的变量称之为全局变量，可以被函数内部调用。
但不随意更改全局变量的值，直接修改会报错，若想修改必须添加 global 这个声明。
-------- 区分两种状态 ----"变量名不同"函数内部修改 ---- "变量相同"函数内部修改 ----
函数内部的变量与外部同名时，内部变量优先。
此时，想在函数内部修改外部变量的值，需要 nonlocal 这个声明。

"""
""" 
            闭包 
闭包使得局部变量在函数外被访问成为可能

函数外部，是不可以访问函数内部的局部变量。
需要内部函数去将结果返回给内部作用域。


"""

def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of  # 返回值是 exponent_of 函数

square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方

print(square(2))  # 计算 2 的平方
print(cube(2))  # 计算 2 的立方

"""
外部是无法
"""
def print_msg():  # print_msg 是外围函数
    msg = "zen of python"
    def printer():  # printer 是嵌套函数
        print(msg)
    return printer

another = print_msg() # print_msg(printer(print(msg))
""""""
# 输出 zen of python
another()
