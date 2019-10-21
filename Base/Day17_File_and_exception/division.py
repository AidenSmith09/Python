# /bin/etc/env Python
# -*- coding: utf-8 -*-

print("给我2个数字，我将他们分开")
print("Enter 'q' to quit")

while True:
    first_number = input("\n第一个数字：")
    if first_number == 'q':
        break
    second_number = input("第二个数字")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("你不能输入0")
    else:
        print(answer)

"""
没有异常处理的代码

print("给我2个数字，我将他们分开")
print("Enter 'q' to quit")
while True:
    first_number = input("\n第一个数字：")
    if first_number == 'q':
        break
    second_number = input("第二个数字")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
"""