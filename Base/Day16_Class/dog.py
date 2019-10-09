# /bin/etc/env Python
# -*- coding: utf-8 -*-
# 学习类之前，先学习面向对象的概念。
'''



'''


class Dog():  # 根据类来创建对象，被称之为实例化。可以理解为文档的模板。
    def __init__(self, name, age):  # 这是一个特殊的方法，第一个参数永远是self。有了它，在创建‘实例对象’的时候，就不能传入空的参数了。
        """
        初始化属性name 和 age；
        初始化的意思是：创建新变量后为变量赋值后的流程，叫初始化。变量赋为默认值，把控件设为默认状态，把没准备的准备好
        如a = 1，单拿a出来，这个a变量没有任何有效性故不能使用。

        这是类的方法。
        """
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)  # 创建一个实例对象
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()  # 对象访问属性
my_dog.roll_over()  # 对象访问属性

your_dog = Dog('lucy', 3)
print("\nYour dog's name is "+your_dog.name.title()+".")
print("your dog is "+str(your_dog.age)+" years old.")
your_dog.sit()


"""
如何区分“类的方法”和”普通函数“？
它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
"""
