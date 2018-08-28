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
print("-------------if else--------------")
#if else
age = 17
# if else 语句
if age >= 18:
    print('you are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

print("------------if elif else-----------------")
# if elif else 语句
# 如：4岁以下免收费，4～18收费5$，18岁(含)以上收10$
age = 16
if age < 4:
    print("you admission cost is $0")
elif age < 18:
    print("you admission cost is $5")
else:
    print("you admission cost is $10")


print("------------多 if elif else-----------------")
# 多 if else 语句
# 例题 4岁以下免费，65岁以上，18岁以下半价
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("You admission cost si $" + str(price) + ".")
print("------------省略else-----------------")
# 省略else
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("You admission cost si $" + str(price) + ".")

print("------------多条件实例-----------------")
# 多条件实例 如：披萨店点餐，客户只点了两种配料，哪就需要在披萨中包含这些配料
# 受限创建一个列表，用来存储客户选择的配料
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

