# /bin/etc/env Python
# -*- coding: utf-8 -*-

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string+= line.strip()
print(pi_string[:52]+"……")
print(len(pi_string))

birthday = input('输入你的出生日期，在圆周率中查找，格式 mmddyy：')
if birthday in pi_string:
    print("存在")
else:
    print("不存在")