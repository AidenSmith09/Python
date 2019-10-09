# /bin/etc/env Python
# -*- coding: utf-8 -*-
class Dog():  # 根据类来创建对象，被称之为实例化
    def __init__(self, name, age):
        """初始化属性name 和 age；初始化的意思是：函数中仅出现了变量名。
        如a = 1，单拿a出来，这个a变量没有任何有效性故不能使用。
        所以在函数中给变量赋值或引用的过程叫做初始化。
        """
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy',3)
print("\nYour dog's name is "+your_dog.name.title()+".")
print("your dog is "+str(your_dog.age)+" years old.")
your_dog.sit()