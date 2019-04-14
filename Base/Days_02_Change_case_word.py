# /bin/etc/env Python
# -*- coding: utf-8 -*-
name = 'add lovelace'
print(name.title())
"""
name后的'.'是Python对变量name使用'title()'方法的操作。每个方法后都会跟一个'()'。
因为方法需要额外的信息才能工作，而额外的信息就在括号内。
在本案例中，tittle()不需要额外信息，因此括号中是空的。
"""
print(name.upper())
print(name.lower())
# lower方法对于存储数据很管用，很多时候我们无法依靠用户来提供正确大小写。
# 因此先将字符串转换为小写，再将其转换为最合适的大小写数据。

# 字符串拼接
first_name = "ada"
last_name = "lovelaca"
full_name = first_name + " " + last_name
print(full_name)
print("Hello " + full_name.title() + "!")
# 每次这样输出很麻烦，所以存储到一个变量中。
message = "Hello " + full_name.title() + "!\n"
print(message)

# 制表符使用方式
# \n代表这换行
print("Languager:\nPython\nC\nJavaScript\n")
print("Languager:\n\tPython\n\tC\n\tJavaScript\n")

# 删除空白
print('不带空格的' + 'python。')
print('携带空格的' + 'python 。')
print('加句号可以看的更清楚')
"""
在程序中，print输出的是两种数据。如果你不告诉Python，Python会认为它是有意义的。
当我们对比两个字符是否相同的时候，会判定是不通的。
比如在用户登录时，检查用户名。留白与不留白的区别就显而易见了。
"""
favorite_language = 'python '
print('临时删除空白的' + favorite_language.rstrip())
print('恢复删除之前的' + favorite_language)
# 仔细观察两个输出结果。发现空白被删除其实是临时的。
# 所以需要把结果返回到变量中。
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = '  Python '
print(favorite_language)
favorite_language = favorite_language.lstrip()
favorite_language = favorite_language.strip()
print("被剔除前后空白的" + favorite_language)

IP = " Aiden Smith "
IP = IP.lstrip()  # 去除左边的空白
IP = IP.rstrip()  # 去除右边的空白
print(IP)

S_IP = " Aiden Smiht "
S_IP = S_IP.strip()  # 去除中间空格
print(S_IP)
print(S_IP.count('A'))
print(len(S_IP))




######## 总结 ######
"""
在Python中 Str 字符串类型的操作
title()     将首字母大写
lstrip()    删除左边的空格
rstrip()    删除右边的空格
strip()     删除中间的空格
count()     计算字符串中，有几个相同字符。（需带参）
len()       计算字符串的长度
"""