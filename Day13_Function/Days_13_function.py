# /bin/etc/env Python
# -*- coding: utf-8 -*-

def greet_user():
    print("Helle")


greet_user()

"""
当函数被定义后，直接调用函数即可输出函数中的内容
"""


def greet_user1(username):
    print("Hello," + username.title() + "!")


greet_user1('jesse')
greet_user1('harry')  # 二次调用
"""
上例子中，
username 称之为形参，为实际数据做一个外号，外号是可以被很多人使用的。
jesse 称之为实参，可以理解为人名，实质的真实的数据。即为实参数
函数被创建后，可多次被使用（调用）。
"""


def describe_pet(animal_type, pet_name):
    print("\n我有一只" + animal_type + ".")
    print("我的" + animal_type + "名字叫" + pet_name + ".")


describe_pet('harry', '仓鼠')
"""
开发中要主要形参与实参的位置。
若顺序搞混，会导致传参出错。
这也许是个小问题，但是再庞大的数据开发数据中，真的有可能发生。
"""
print("---")
describe_pet(pet_name="harry",animal_type='仓鼠',)  # 关键字实参
"""
在调用中，形参与实参进行绑定，则无需考虑实参的顺序问题。
"""


def describe_pet1(pet_name, animal_type='狗'):
    print("\n我有一只" + animal_type + ".")
    print("我的" + animal_type + "名字叫" + pet_name + ".")


describe_pet1(pet_name='HaHa')
describe_pet1(pet_name='毛毛' , animal_type='猫')  # 我虽然指定了默认值，但默认值不是不能更改
"""
这里需要注意一点，给形参制定默认参数时，带默认值的形参必须在后，否则报错。
错误展示：def describe_pet1(animal_type = '狗',pet_name):
"""


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
"""
看不懂？？
没关系，举个简单的例子:
***********************不带返回值***********************
def showcode(x):
    print(x)  # 不同之处在于此
d = showcode(3) #此处显示的结果，是因为调用了函数。函数中Print为显示结果。
print(d)
***********************带返回值*************************
def show_code(a):
    return a  # 不同之处在于此
dd = show_code(6)
print(dd)

说一下他们之间的区别：
不带返回值的函数，仅仅是print代码结果，print不具备存储功能。
带返回值的函数，是将实参传递到调用者手中。这个结果是可存储的

"""
