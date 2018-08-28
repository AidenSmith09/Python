# if条件判断语句
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())  # upper() 全大写
    else:
        print(car.title())

# 条件判断的特点
print("\n")

car = 'BMW'
print('相同情况下的判断：')
print(car == 'BMW')

print('\n与小写的自己的判断：')
print(car == 'bmw')

print('\n区分不同的自己判断结果：')
print(car == 'Bmw')
print('\n将大写全部转换成小写后判断：')
print(car.lower() == 'bmw')

# 不相等判断
A = '1'
if A != '2':
    print("\n数字1不等于数字2")

# 数字比较
answer = 17
if answer != 43:
    print("This is not the correct answer. Please try again!")

# 多条件判断
if 2 != 1:
    print("Turn")
# 使用 and 判断两个条件
# 同时满足则才通过
age_0 = 22
age_1 = 18
print('同时满足两个条件的结果：')
print(age_0 >= 21 and age_1 >= 21)

# 使用 or 判断两个条件
# 指一个满足即可通过
print('同时满足一个条件的结果：')
print(age_0 >= 21 or age_1 >= 21)


# 检查特定的内容是否包含在列表里
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
print('检查特定的内容是否包含在列表里:')
print('mushrooms' in requested_toppings)

# 检查特定的内容不包含在列表里
# 使用 not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")
# 首字大写输出