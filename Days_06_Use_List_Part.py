#切片
#故名思议截取片段。从列表中截取。
#反复的循环操作，造成了资源与时间的浪费。
#故使用切片进行截取。
#如截取前三个元素，常规操作使用for循环。
"""
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
for i in range(3):
    print(players[i])
"""
#使用切片则简单的多
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3]) #从0开始到2，下表不包含3
print(players[2:4]) #从2开始到4，不包含4
print(players[:2]) #默认从0开始，不包含2
print(players[0:]) #下表0开始
print(players[-3:]) #倒数三个元素

print('\n')

#遍历列表
print("Here are the first three playse on my team:")
for player in players[:3]: #循环0-3不包含3，依次存储至player。
    print(player.title())

#Copy列表
#有时操作需要复制数据进行。

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

"""
错误的Copy
以下这种写法仅仅是将 fater 的值关联给 son ，而不是赋值。
关联：A的值改变，B会随着改变
赋值：A的值改变，B不会改变
或者也可以理解成，一个元素，拥有两个变量。
"""
fater = ['A', 'B', 'C']
son = fater
print(fater)
print(son)
fater.append('D')
print(fater)
print(son)


#元组
#不可修改的列表，就是"元组"
#注意：元组是是圆括号()，列表是方括号[]
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 300
#执行后报错，TypeError: 'tuple' object does not support item assignment

#遍历元组
print("遍历元组：")
for vluse in dimensions:
    print(vluse)

#修改元组变量
#前边提过，元组的变量是无法修改的，为什么这里又能说修改呢？
#的确，元组中的元素是不能修改，但是却没有说元组不能被重新赋值

dimensions = (500,499)
print("被重新赋值的元组:")
for vluse in dimensions:
    print(vluse)