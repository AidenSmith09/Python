# /bin/etc/env Python
# -*- coding: utf-8 -*-

temp = "Aiden"
a = dir(temp)
b = type(temp)
c = help(type(temp))
print(a, b, c)
# command + 左键可以看到函数的详细功能
# dir 看类型能做那些操作
# type 查看属类型
# help 查看操作的详细信息
n1 = 123
n2 = 456
print(n1 + n2)
print(n1.__add__(n2))
