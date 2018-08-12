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
# 使用 and 判断两个条件都是True
