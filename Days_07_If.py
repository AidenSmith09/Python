# if条件判断语句
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())  # upper() 全大写
	else:
		print(car.title())

# 条件判断的特点
print("\n")
car = 'bmw'
print(car == 'bmw')

cat = 'audi'
print(car == 'BMw')
