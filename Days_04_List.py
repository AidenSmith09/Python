list = ['A', 'B', 'C', 'D']
print(list)
# So 如此输出会吧列表中的内容，包括标点符号都输出到界面。
# 那是不是可以理解为，此次输出，输出的是list变量，而不是数组。
# 但是严格来讲，此次输出依旧是列表，只不过是列表的内部表现形式。


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[2])
print(bicycles[0].title())
print(bicycles[-1])

"""
输出列表 bicycles[3] 中的数字称之为下标（又称之为索引），下标从0开始。
Python中特殊语法，下标制定为-1代表列表中最后一个元素。
比如在不知道列表长度的情况下，访问返回最后一个元素。
"""
# ------使用列表中的值-------
message = "My first bicycle was a " + bicycles[0].title()
print(message)
A = "张三"
B = "李四"
C = "王五"
name = [A, B, C]
print(name[0] + "Helle world")
print(name[1] + "Helle world")
print(name[2] + "Helle world")

# 对元素的增删改


# 修改元素
# 更改列表中的元素，可以通过给下标重新赋值

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 添加元素
# 最简单的办法在末尾添加一个元素。oppend()方法
motorcycles.append('ducati')
print(motorcycles)

# 插入元素
# 使用 insert() 方法。指定下标后，数据在下标出插入，源数据右移一位
motorcycles.insert(0, 'BMW')
print(motorcycles)

# 删除元素
# del语句 删除元素的条件是知道元素的下标。
print('\n')
print("-----我是华丽分割线：删除的第一种方法-------")
del motorcycles[1]

print(motorcycles)

print('\n')
print("-----我是华丽分割线：删除的第二种方法-------")
# pop() 方法删除的数据可以复用
"""
第一个print 输出结果，是目前 motorcycles 中的列表
第二个print 输出结果是删除掉的结果
第三个print 输出的是pop()方法删掉的值

一般用于被删除的数据二次使用。
例如：获取怪物被杀死的x，y坐标，在此基础上显示爆炸效果。
"""
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles.title())
"""
同时pop()方法可以删除列表中任何位置的元素。但前提是需要知道索引。
可以看到经过程序的顺序执行，motorcycles列表中的内容已经被删除到只剩两个。
"""
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '!')
print(motorcycles)
print('\n')
# 两种删除使用区别：如果删除的元素不再使用，就用 del语句。删除元素后继续使用，就用 pop() 方法

# 根据值删除元素
print("-----我是华丽分割线:根据值删除列表-------")
"""
使用remove()方法删除，在不知道下标的情况下，根据值来进行删除。
"""
motorcycles.insert(0, 'ducati')
motorcycles.insert(0, 'BMW')
print(motorcycles)  # 复原数据

motorcycles.remove('ducati')  # 直接删除
print(motorcycles)

too_expensive = 'yamaha'  # 将需要的二次使用的数据存入一个变量
motorcycles.remove(too_expensive)  # remove通过使用变量来删除，但是变量没有被删
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.\n")  # 系统调用变量，故变量还可使用。

# 列表排序
"""

"""
# sort()方法对列表进行永久排序
# sort(reverse=True)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # 按照字母永久排序，无法逆回原来顺序
print(cars)
cars.sort(reverse=True)  # 添加参数后，执行反向排序
print(cars)
print('\n')

# sorted()临时排序
print("这里原列表：")
print(cars)

print("\n这里是sorted列表:")
print(sorted(cars))

print(sorted(cars, reverse=True))  # sorted中可以添加反向参数。

print("\n这里再次输出原列表:")
print(cars)

# 反向打印
# 目前源List是数据排列是反向。但我不想改变元素顺序，只想倒着打印出来。
# reverse()方法提供了这一功能
cars.reverse()
print(cars)

name = ['A', 'C', 'B', 'D']
print(name)
name.reverse()
print(name)

# 确认列表长度
print("列表的长度" + len(name).__str__())

"""
总结
列表名称[数字] 可以输出下表的元素
bicycles[0].title() 首字母大写

motorcycles.append('ducati') 在列表末尾添加一个元素
motorcycles.insert(0,'BMW') 在下标位置，写入数据。其余源数据右移一位。
del motorcycles[1] Del语句永久删除数据，需要指定下标。
motorcycles.pop()  删除数据可以存于变量，默认最后一个。
motorcycles.remove('ducati') 根据元素值来进行删除，可填写变量。

cars.sort() 按照字母永久排序，无法逆回原来顺序
cars.sort(reverse=True) 添加参数后，执行反向排序
sorted(cars) 临时排序
sorted(cars,reverse=True) 临时反向排序
cars.reverse() 反向输出元素。列表内元素数据
"""
