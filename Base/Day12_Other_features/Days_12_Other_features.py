# /bin/etc/env Python
# -*- coding: utf-8 -*-

# 制定解释权，制定编码。


# enumerate 默认从0开始自增1，可+参数 start = 1
# li = ['computer', "moues", 'USB', 'car']
# for key, item in enumerate(li, 1):  # +参从1开始
#     print(key, item)
#
# inp = input("请输入商品")
# inp_num = int(inp)
# print(li[inp_num - 1])
#
# leee = len(li)
# for i in range(0, leee):
#     print(i, li[i])

"""
小练习

有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
"""
# 第一种写法
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# 生成一个字典，"k1":[11,22,33,44,55]
l1 = []
l2 = []
for i in li:
    if i <= 66:
        l1.append(i)
    else:
        l2.append(i)
temp = {"k1": l1, "k2": l2}
print(temp)

# 第二种写法
dic = {"k1": [], "k2": []}
for i in li:
    if i <= 66:
        dic["k1"].append(i)
    else:
        dic["k2"].append(i)
print(dic)

"""
查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
"""
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

for i in li:
    new_i = i.lstrip()
    if new_i.endswith('c') and new_i.startswith('a') or new_i.endswith('A'):
        print(i)