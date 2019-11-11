# /bin/etc/env Python
# -*- coding: utf-8 -*-


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

    def sit(self):  # 特别注意缩进
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)  # 创建一个实例对象
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()  # 对象访问属性
my_dog.roll_over()  # 对象访问属性

your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


class Car():  # 创建模板过程
    """ 给定实参"""

    def __init__(self, make, model, year):  # 初始化参数
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 实参可以不添加在（），因为它有实际参数。不需要初始化。

    def get_descriptive_name(self):  # 创建方法。属性有了，做什么也要跟上。
        long_name = str(self.year) + ' ' + self.make + ' ' + \
            self.model  # 赋值的时候参数类型要相同，否则报错。
        return long_name.title()

    def read_odometer(self):
        print("This cat has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):  # 使用方法修改
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你不能回调里程表")

    def increment_odometer(self, miles):  # 顺序读取，所以前边的里程已经给定，所以会直接获取原有里程。通过方法进行累加。
        """增加定额"""
        self.odometer_reading += miles

    def fill_gas_tank(self, litre):
        """汽油油箱"""
        self.liter = litre
        print("油箱剩余油量" + str(self.liter) + "L")


my_new_car = Car('audi', "A8L", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

my_new_car.odometer_reading = 23  # 直接修改属性的值
my_new_car.read_odometer()

my_new_car.update_odometer(16)  # 通过方法修改。
my_new_car.read_odometer()

print("----------- 新实例输出 ---------------")
used_car = Car('BMW', 'A1', 2011)       # 创建一个新的实例
print(used_car.get_descriptive_name())  # 打印出我的旧汽车
used_car.update_odometer(23500)         # 输入已有的里程
used_car.read_odometer()                # 读取历程
used_car.increment_odometer(100)        # 我卖车期间开了100公里，额定增加100
used_car.read_odometer()
used_car.fill_gas_tank(100)

"""
类的继承
如果我每次要用到类，都需要写一次无疑是很累的。所以类是可以"继承"下去的。
当A继承B时，A将自动获得B的所有"属性"和"方法"。
B则称之为"父类"
A则称之为"子类"，子类同时还可以拥有"自己的属性和方法"。

"""


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("这是这辆车的 " + str(self.battery_size) + "-kWh 电量。")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 280
        else:
            range = "请输入电量"
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """子类必须位于父类之后，必须在括号里填写父类名称"""

    def __init__(self, make, model, year):      # 接收父类的信息
        super().__init__(make, model, year)     # 将父类与子类关联
        self.run_km = 300                       # 子类私有属性添加默认值。
        self.battery = Battery()                # 将类作为属性

    def run_km_h(self):
        """调用私有属性"""
        print("车辆剩余公里为 " + str(self.run_km) + "km/h")

    def fill_gas_tank(self, litre):  # 必须跟父类方法相同。
        """父亲类方法重写"""
        print("电车没有油箱")

my_tesla = ElectricCar('Tesla', 'model S', 2019)  # 实例调用子类
print(my_tesla.get_descriptive_name())  # 子类调用父类中的方法
my_tesla.run_km_h()                     # 子类私有属性
my_tesla.fill_gas_tank(100)             # 父类方法重写后的调用
my_tesla.battery.describe_battery()     # 将类作为属性后调用
my_tesla.battery.get_range()

"""
如何区分“类的方法”和”普通函数“？
它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。


注意：
注意类中函数的缩进
注意调用方法时不要调用错误。有时候名字错误，则有可能调用错误。(新手常犯)
"""
