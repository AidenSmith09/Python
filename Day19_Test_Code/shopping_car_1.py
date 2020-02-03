# /bin/etc/env Python
# -*- coding: utf-8 -*-
money = int(input("请输入总资产："))
all_price = 0
cat_dir = {}
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "显卡", "price": 998},
]

while True:
    for key, item in enumerate(goods, 1):  # 为了给字典带编号，所以需要使用enumerate
        print(key, item["name"], item["price"])  # 每一个元素获取到位，即每一个字典获取到位

    choose_goods = int(input("请选择商品(其余数字则进行结算):"))


    # print("选择的商品是",car_list['name'])

    if 0 <= int(choose_goods) < 5:
        car_list = goods[choose_goods - 1]
        # print(car_list['name'])
        name = car_list['name']
        if name in cat_dir.keys():
            '''判断商品是否存在于购物车中'''
            cat_dir[name]['num'] += 1
        else:
            cat_dir[name] = {"num": 1, "single_price": car_list['price']}

        for x, y in cat_dir.items():
            n = y['single_price']
            m = y['num']
            all_sum = m * n
            all_price += all_sum
            print(
                x,
                "单价:",
                y["single_price"],
                "数量",
                y["num"],
                "\n您的总额",
                money,
                "购物车总价",
                all_price)

    else:
        if all_price < money:
            print("购买成功")
            money -= all_price
            print("您的余额还有:", money)
        else:
            print("你的钱不够")
            break
