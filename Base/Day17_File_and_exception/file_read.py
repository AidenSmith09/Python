# /bin/etc/env Python
# -*- coding: utf-8 -*-
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

""" 循环打印每行内容 """
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
# 发现打印出后有空行，是因为在文件中，每行莫问都有一个/n，print打印时又追加了一个。
# 所以打印时会产生2个/n 换行符。



""" 创建一个包含文件各行内容的列表，依旧使用pi_digits.txt"""
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())


""" 使用文件的内容 """
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = '' # 创建空变量，用于存储值
for line in lines: # 循环列表
    pi_string+=line.strip()  # 将循环的列表的值存储在变量中。
print(pi_string) # 值的类型为字符串
print(len(pi_string))
