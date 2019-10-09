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

# bit_length() 获取二进制的最短位数
n1 = 4  # 00000100
ret = n1.bit_length()
print(ret)

a1 = "alden is alph1"
ret = a1.count('al')
print(ret)


a1.isalpha()  # 检验内容是否是字母
a1.istitle()  # 判断是不是标题
print(a1.replace("al", "ai"))  # 替换内容


# 查看源码时
# 只有一个self表示无需传参，可以直接调用
# 有两个 self 表示最多可传两个参数，同时会规定默认值。
# 当不知道传几个参数是，查看源码。