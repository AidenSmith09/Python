# /bin/etc/env Python
# -*- coding: utf-8 -*-
def make_pizza_2(size, *toppints):
    print("\nMaking a " + str(size) + "- inch pizza with the following toppings:")
    for topping in toppints:
        print("- " + topping)

def frommodule_name_one():
    print('异目录导入包，未设置别名的函数1')

def frommodule_name_two():
    print('异目录导入包，设置别名的函数2')