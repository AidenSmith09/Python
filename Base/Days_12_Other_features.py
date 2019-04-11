# /bin/etc/env Python
# -*- coding: utf-8 -*-

# 制定解释权，制定编码。


# enumerate 默认从0开始自增1，可+参数 start = 1
li = ['computer', "moues", 'USB', 'car']
for key, item in enumerate(li, 1):  # +参从1开始
    print(key, item)

inp = input("请输入商品")
inp_num = int(inp)
print(li[inp_num - 1])

leee = len(li)
for i in range(0, leee):
    print(i, li[i])
