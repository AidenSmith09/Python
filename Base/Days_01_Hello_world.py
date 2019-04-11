# /bin/etc/env Python
# -*- coding: utf-8 -*-
# 指定解释权，制定编码。


print("Hello,world")
message = 'Hello Python world'
print(message)
# 变量名称只能由字母、数字、下划线。数字不能开头。不能包含空格。
# 不能使用函数名称、Python关键字。

message = "hello Pyhon Crash Course reader!"
print(message)
# 变量是可以被替换的。
message = '中文'
print(message)
print('中文')
# Python3可以直接输入中文了

English = 'I told my friend,"Python is my favorite language!"'
print(English)
English = "The language 'Python' is named after Monty Python, Not the snake"
print(English)
print('两种引号随意嵌套。双引号嵌套单，单引号嵌套双。')

"""
Python2 使用的是 ASCII (所以无法输入中文)
Python3 默认使用 utf-8

ASCII -> unicode -> gbk,utf-8
ASCII - 一个字节，8位
unicode -> 最少两个字节，16位
utf-8 -> 用多少表示多少，但3个字节表示一个中文
gbk -> 2个字节表示一个中文
"""
