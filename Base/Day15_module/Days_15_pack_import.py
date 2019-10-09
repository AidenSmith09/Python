# /bin/etc/env Python
# -*- coding: utf-8 -*-


def make_pizza(*topings):  # 星号的作用是创建一个空元组
    print("\nMaking a pizza with the following topings:")
    for topings in topings:
        print("- " + topings)

def function_one():
    print('同目录导入函数1')


def function_two():
    print('同目录导入，设置别名的函数2')