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
username 称之为形参
jesse 称之为实参
函数创建后，可多次被调用，
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
describe_pet(animal_type= '仓鼠', pet_name="harry")  # 关键字实参
"""
在调用中，形参与实参进行绑定，则无需考虑实参的顺序问题。
"""

def describe_pet1(pet_name,animal_type = '狗'):
    print("\n我有一只" + animal_type + ".")
    print("我的" + animal_type + "名字叫" + pet_name + ".")
"""
这里需要注意一点，给形参制定默认参数时，带默认值的形参必须在后，否则报错。
错误展示：def describe_pet1(animal_type = '狗',pet_name): 
"""
describe_pet1(pet_name='HaHa')