# /bin/etc/env Python
# -*- coding: utf-8 -*-

money = int(input("请输入总资产："))
all_price = 0
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "显卡", "price": 998},
]

for o,i in enumerate(goods,1):
    print(o,i['name'], i['price'])

car_dict = {}
while True:
    choose = input("请选择商品(Y结算)：")
    if choose.lower() == "y":
        break

    for item in goods:
        """次循环内，查找商品是否存。"""
        if item['name'] == choose:
            '''判断输入商品是否存在'''
            print("您选择了：", item['name'])
            name = item['name']
            if name in car_dict.keys():
                '''判断商品是否存在于购物车中'''
                car_dict[name]['num'] += 1
            else:
                car_dict[name] = {"num": 1, "single_price": item['price']}

    for x, y in car_dict.items():
        print(x, "单价:", y["single_price"], "数量", y["num"])



