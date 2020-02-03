# /bin/etc/env Python
# coding: utf-8


"""
功能要求：

要求用户输入总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
附加：可充值、某商品移除购物车
goods = [
  {"name": "电脑", "price": 1999},
  {"name": "鼠标", "price": 10},
  {"name": "游艇", "price": 20},
  {"name": "美女", "price": 998},
]
"""

"""
money = input一个总的资产，用于存储。

"""
money = input("请输入总资产：")

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "显卡", "price": 998},
]

# # 列表中的元素是一个字典。
# # 循环列表，获取元素
# for key, item in enumerate(goods):  # 为了给字典带编号，所以需要使用enumerate
#     print(key, item["name"], item["price"])  # 每一个元素获取到位，即每一个字典获取到位
#
# # 创建一个shopping 购物车
# # 将选择商品元append至购物车列表中。



while int(money) > 10:
    for key, item in enumerate(goods):  # 为了给字典带编号，所以需要使用enumerate
        print(key, item["name"], item["price"])  # 每一个元素获取到位，即每一个字典获取到位

    choose_goods = input("请选择商品：")
    shopping = []
    shopping.append(goods[int(choose_goods)])
    for i in shopping:  # 打印购物车中的字典
        if i["price"] < int(money):
            print(i["name"], i["price"],"元","购买成功")
            money = int(money) - i["price"]
            print("剩余资产", money, "\n")
            shopping.clear()
        else:
            print("余额不足")
            a = input("请问是否充值 yes or no：")
            if a == "yes":
                i = input("充值钱数：")
                money = int(money) + int(i)
                print("充值成功,现有资产", money, "\n")
            else:
                print("没钱还想买东西？")
                break
