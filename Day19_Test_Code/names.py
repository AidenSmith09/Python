# /bin/etc/env Python
# -*- coding: utf-8 -*-
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")

while True:
    first = input("\n请输入 first name：")
    if first == 'q':
        break
    last = input("请输入名 last name: ")
    if last == 'q':
        break
    middle = input("请输入middle name：")
    if middle == 'q':
        break

    fromatted = get_formatted_name(first, last, middle)
    print("\t格式整齐的名称： " + fromatted + ".")
